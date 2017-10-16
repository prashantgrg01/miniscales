from django.shortcuts import render
from .forms import KeyForm
from .music_scale import MusicScale

# Create your views here.
# Main View
def index(request):
    # handle the post request
    if request.method == "POST":
        # bind new form to the form in POST request
        form = KeyForm(request.POST)

        # get the key and scale from the request
        key = request.POST.get("key", "")
        scale = request.POST.get("scale", "")

        # initialize the core MusicScale class
        ms = MusicScale()
        
        # get the note_name, scale_name and scale_pattern
        note_name = key
        scale_name, scale_pattern = ms.getScaleNameAndPattern(scale)
        
        # get the notes in the scale
        scale_notes = ms.getNoteScale(key, scale)
        # create the note numbers list
        note_nums = []
        for i in range(len(scale_notes)):
            note_nums.append(str(i+1))
        # add the '/1' to the octave note number
        note_nums[len(scale_notes) - 1] += "/1"

        # get the chords in the scale
        scale_chords = ms.getScaleChords(scale_notes)
        # get chords display version
        scale_chords = getChordsDisplayVersion(scale_chords)

        return render(request, "ms/index.html", {"form": form, "note_name": note_name, "scale_name": scale_name, "scale_pattern": scale_pattern, "note_nums": note_nums, "scale_notes": scale_notes, "scale_chords": scale_chords})
    # handle the get request
    else:
        # create blank form and render it
        form = KeyForm()
        return render(request, "ms/index.html", {"form": form})

# function to take a dict of chords and return a displayable version
def getChordsDisplayVersion(chords):
    assert type(chords) == dict, "chords must be a dict!"
    # initialize an empty display_chords dict
    display_chords = {}
    # for each key in chords dict
    for key in chords.keys():
        # add the key to the display_chords dict
        display_chords[key] = []
        # for each chord in the key
        for chord in chords[key]:
            # check if the key is flat or sharp and get the chord_type
            if len(key) == 1:
                chord_type = chord[1:]
            else:
                chord_type = chord[2:]
            # then check the chord_type and create a corresponding chord_name for display
            if chord_type == "minMaj7":
                chord_name = key + "min<sup>maj7</sup>"
            elif chord_type == "hdim7":
                chord_name = key + "<sup>&#8709;7</sup>"
            elif chord_type == "fdim7":
                chord_name = key + "<sup>&#9898;7</sup>"
            elif chord_type == "augMaj7":
                chord_name = key + "aug<sup>maj7</sup>"
            else:
                chord_name = chord
            # append the chord_name to the current key in the display_chords dict
            display_chords[key].append(chord_name)
    # return the display_chords dict
    return display_chords

