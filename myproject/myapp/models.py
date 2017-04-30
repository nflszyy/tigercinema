# -*- coding: utf-8 -*-
from django.db import models
from .validators import validate_mime_type
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating


class Document(models.Model):
    fname = models.CharField(max_length = 100)
    lname = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    thumbnail = models.CharField(max_length = 100)
    description = models.TextField()
    GENDER_CHOICES = (
                      ('1', 'Narrative'),
                      ('2', 'Documentary'),
            )
    choice = models.CharField(max_length = 1,choices=GENDER_CHOICES,default = '1')
    docfile = models.FileField(upload_to='documents/%Y/%m/%d', validators=[validate_mime_type])
    ratings = GenericRelation(Rating, related_query_name='documents')

