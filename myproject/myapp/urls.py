# -*- coding: utf-8 -*-
from django.conf.urls import url
from myproject.myapp import views

urlpatterns = [
    url(r'^welcome/$', views.welcome, name='welcome'),
    url(r'^homepage/$', views.homepage, name='homepage'),
    url(r'^documentary/$', views.documentary, name='documentary'),
    url(r'^narrative/$', views.narrative, name='narrative'),    
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^uploadform/$', views.uploadform, name='uploadform'),    
    url(r'uploadsuccess/$', views.uploadsuccess, name='uploadsuccess'),
    url(r'^delete/$', views.delete, name='delete'),    
]
