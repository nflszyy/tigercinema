# -*- coding: utf-8 -*-

#this is the button with which you choose file from pc
from django import forms
from .validators import validate_mime_type

class DocumentForm(forms.Form):
    fname = forms.CharField(max_length = 100, label='Your first name')
    lname = forms.CharField(max_length = 100, label='Your last name')
    title = forms.CharField(max_length = 100, label='Title of your movie')
    description = forms.CharField(widget = forms.Textarea, label="Short description of your work:")
    choice = forms.ChoiceField(choices=[("1", "Narrative"), ("2", "Documentary")], label="Choose a type")
    docfile = forms.FileField(label='Upload your movie here',validators=[validate_mime_type])