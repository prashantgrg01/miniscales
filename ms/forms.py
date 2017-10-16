from django import forms
from .music_scale import MusicScale

# form class for our key form that is to be displayed to the user
class KeyForm(forms.Form):
    ms = MusicScale()
    # get all the possible key choices
    key_choices = ms.getNoteOptions()
    # append the initial value to the front of the list
    key_choices.insert(0, ("", "Key"))
    # create the key choice form field
    key = forms.ChoiceField(choices=key_choices, required=True, widget=forms.Select(attrs={"name": "key", "id": "key", "class": "form-control"}))
    # get all the possible scale choices
    scale_choices = ms.getScaleOptions()
    # append the initial value to the front of the list
    scale_choices.insert(0, ("", "Scale"))
    # create the scale choices form field
    scale = forms.ChoiceField(choices=scale_choices, required=True, widget=forms.Select(attrs={"name": "scale", "id": "scale", "class": "form-control"}))
