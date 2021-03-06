# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating
from s3direct.fields import S3DirectField
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

class Document(models.Model):
    fname = models.CharField(max_length = 100)
    lname = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    netid = models.CharField(max_length = 100)
    description = models.TextField()
    GENRE_CHOICES = (
                      ('1', 'Narrative'),
                      ('2', 'Documentary'),
            )
    choice = models.CharField(max_length = 1,choices=GENRE_CHOICES,default = '1')
    thumbnail = S3DirectField(dest='thumbnails', blank=True)
    docfile = S3DirectField(dest='videos', blank=True)
    ratings = GenericRelation(Rating, related_query_name='documents')


