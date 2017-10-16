"""
Definition for the main MusicScale class
"""
class MusicScale(object):
    def __init__(self):
        # List of all the musical notes and their total count
        self.notes = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
        self.notes_length = 12
        # a dict of supported scales with their names and patterns
        self.scales = {
            "maj": {"name": "Major", "pattern": ["w","w","h","w","w","w","h"]},
            "min": {"name": "Natural Minor", "pattern": ["w","h","w","w","h","w","w"]},
            "hmin": {"name": "Harmonic Minor", "pattern": ["w","h","w","w","h","wh","h"]},
            "mmin": {"name": "Melodic Minor", "pattern": ["w","h","w","w","w","w","h"]},
            "majp": {"name": "Major Pentatonic", "pattern": ["w","w","wh","w","wh"]},
            "minp": {"name": "Minor Pentatonic", "pattern": ["wh","w","w","wh","w"]},
            "blues": {"name": "Blues", "pattern": ["wh", "w", "h", "h", "wh", "w"]}
        }
        # a dict of supported chords with their formulas
        self.chords = {
            "maj": ["1", "3", "5"],
            "min": ["1", "b3", "5"],
            "dim": ["1", "b3", "b5"],
            "aug": ["1", "3", "5#"],
	        "sus2": ["1", "2", "5"],
            "sus4": ["1", "3#", "5"],
            "maj7": ["1", "3", "5", "7"],
            "7": ["1", "3", "5", "b7"],
            "min7": ["1", "b3", "5", "b7"],
            "minMaj7": ["1", "b3", "5", "7"],
            "hdim7": ["1", "b3", "b5", "b7"],
            "fdim7": ["1", "b3", "b5", "d7"],
            "augMaj7": ["1", "3", "5#", "7"]
        }
        # a dict of supported intervals
        self.intervals = {
	        "2": 2,
            "b3": 3,
            "3": 4,
            "3#": 5,
            "b5": 6,
            "5": 7,
            "5#": 8,
            "d7": 9,
            "b7": 10,
            "7": 11
        }

    # returns a list of note options
    def getNoteOptions(self):
        # create an empty options list
        options = []
        # add each note from self.notes to options list
        for note in self.notes:
            options.append((note, note))
        return options

    # returns a list of scale options
    def getScaleOptions(self):
        # create an empty options list
        options = []
        # make a tuple of each scale and their corresponding name and add it to the options list
        for scale in self.scales:
            scale_name = self.scales[scale]["name"] 
            options.append((scale, scale_name))
        return options

    # returns the scale name and pattern as strings
    def getScaleNameAndPattern(self, scale_name):
        assert type(scale_name) == str, "scale_name must be a string!"
        # get the scale name from self.scales dict and join it with the note to create the name
        name = self.scales[scale_name]["name"]
        # get the string equivalent from the scale pattern list
        pattern = ""
        for step in self.scales[scale_name]["pattern"]:
            pattern += step + " "
        return (name, pattern[:-1])
    
    # returns the index of the note if it is in self.notes else returns -1
    def getNoteIndex(self, note):
        assert type(note) == str, "note must be a string!"
        found = False
        index = -1
        for i in range(self.notes_length):
            if note == self.notes[i]:
                found = True
                index = i
        return index 

    # returns a list of all the notes in a given scale for a given note
    def getNoteScale(self, note, scale_name):
        assert type(note) == str and type(scale_name) == str, "Both note and scale_name must be strings!"
        # get the index of the note if its in self.notes list else return an error message
        index = self.getNoteIndex(note)
        if index == -1:
            return "Not a musical note!"
        
        # if the note is found, append it to scale_notes list making it the root note
        scale_notes = []
        scale_notes.append(note)
        # get the scale pattern from the self.scales dict
        scale = self.scales[scale_name]["pattern"]
        # for each step in scale, get the next note and append it to scale_notes list
        for step in scale:
            if step == "w":
                index += 2
            elif step == "wh":
                index += 3
            else:
                index += 1
            if index > self.notes_length - 1:
                index -= self.notes_length
            scale_notes.append(self.notes[index])
        # return all the notes in the scale for the given root note along with its octave note
        return scale_notes

    # returns all the notes in a chord of a note
    def getNoteChord(self, note, chord_type):
        assert type(note) == str and type(chord_type) == str, "Both note and chord_type must be strings!"
        chord_notes = []
        # get the index of the root note
        index = self.getNoteIndex(note)
        # for each value in chord formula
        for i in self.chords[chord_type]:
            # if the value represents root note, set the interval to 0 
            # else get the interval that represents the value
            if i == "1":
                interval = 0
            else:
                interval = self.intervals[i]
            # add the interval to index to get the index of next note in the chord
            temp = index + interval
            # if the calculated index exceeds the max index in notes list then adjust it
            if temp > self.notes_length - 1:
                temp -= self.notes_length
            # finally append the note to the chord_notes list
            chord_notes.append(self.notes[temp])
        return chord_notes

    # returns whether the given chord fits(is a valid chord) within a given scale or not
    def isValidChordInScale(self, chord, scale):
        assert type(chord) == list and type(scale) == list, "Both chord and scale must be lists!"
        # initialize valid to True which denotes that the chord fits in the scale
        valid = True
        # i represents the index for each note in the chord
        i = 0
        # while valid is True and i is less than the no. of notes in chord
        while valid and i < len(chord):
            # get a note in the chord
            note = chord[i]
            # if the note doesn't occur in the scale then set valid to False 
            # which denotes that the chord doesn't fit in the scale
            if not note in scale:
                valid = False
            # increase the index value to get the next note in the chord
            i += 1
        return valid

    # returns all the chords that fits into a given scale
    def getScaleChords(self, scale):
        assert type(scale) == list, "scale must be a list!"
        # initialize an empty chord dict
        chords = {}
        # remove the last/octave note from the scale
        scale = scale[:-1]
        # get a copy of all the notes in the scale
        scale_notes = scale.copy()
        # for each note in the scale
        for note in scale_notes:
            # add a key for the current note in the chords dict and initialize it to an empty list
            chords[note] = []
            # for each chord_type in self.chords
            for chord_type in self.chords:
                # get the specific chord for the current note
                chord = self.getNoteChord(note, chord_type)
                # if the chord fits in the scale
                if self.isValidChordInScale(chord, scale):
                    # append the chord to the list under the key of current note
                    chords[note].append(note+chord_type)
        return chords
