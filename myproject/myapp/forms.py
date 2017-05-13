# -*- coding: utf-8 -*-
from django import forms
from .validators import validate_mime_type 

#this is the button with which you choose file from pc
from s3direct.widgets import S3DirectWidget

class DocumentForm(forms.Form):
    fname = forms.CharField(max_length = 100, label='Your first name')
    lname = forms.CharField(max_length = 100, label='Your last name')
    title = forms.CharField(max_length = 100, label='Title of your movie')
    description = forms.CharField(widget = forms.Textarea, label="Short description of your work:")
    choice = forms.ChoiceField(choices=[("1", "Narrative"), ("2", "Documentary")], label="Choose a type")
    thumbnail = forms.URLField(label='Choose thumbnail image',max_length=500,widget=S3DirectWidget(dest='thumbnails'))
    docfile = forms.URLField(label = 'Your Film', max_length = 500, widget=S3DirectWidget(dest='videos'))
