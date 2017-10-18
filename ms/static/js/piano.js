window.addEventListener("load", function() {
    //Add an event listener for mouse click on any piano key and call the keyClicked function
    document.getElementById("piano").addEventListener("click", keyClicked);
    //Add an event listener for touch event on any piano key and call the keyClicked function
    document.getElementById("piano").addEventListener("touchstart", keyClicked);
    
    //keyClicked function which handles the key touched on the piano and passes the respective note to playNote function
    function keyClicked(event) {
        //For test purpose
        //console.log(event.target.parentElement.id);
        
        //Touch or click check function for each individual note
        if (event.target.parentElement.id == "piano") {
            note = event.target.id;
        } else {
            note = event.target.parentElement.id;
        }
        
        // Call the playNote function to actually play the note
        playNote(note)

        event.preventDefault();
        return false;
    }  
    
    //playNote function that actually plays the sound of the corresponding note
    function playNote(note) {
        sound = new Howl({
            urls: ["static/audio/"+note+".mp3"],
            onplay: function() {
                //Make the respective note appear like its clicked
                document.querySelector("#"+note).style.backgroundColor = "#bdc3c7";
            },
            onend: function() {
                //Reset the respective note to appear like its not clicked
                if (note == "note2s" || note == "note2o" || note == "note4s" || note == "note4o" || 
                    note == "note7s" || note == "note7o" || note == "note9s" || note == "note9o" ||
                    note == "note11s" || note == "note11o") {
                    document.querySelector("#"+note).style.backgroundColor = "#222";
                } else {
                    document.querySelector("#"+note).style.backgroundColor = "#fff";
                }
            }
        }).play();
    }
    
});