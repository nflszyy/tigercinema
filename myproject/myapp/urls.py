# -*- coding: utf-8 -*-
from django.conf.urls import url
from myproject.myapp import views
import django_cas_ng.views

urlpatterns = [
    url(r'^welcome/$', views.welcome, name='welcome'),
    url(r'^homepage/$', views.homepage, name='homepage'),
    url(r'^play/(?P<user_id>\d+)/$', views.play, name='play'),
    url(r'^play/$', views.play, name='play'),
    url(r'^documentary/$', views.documentary, name='documentary'),
    url(r'^narrative/$', views.narrative, name='narrative'),    
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^uploadform/$', views.uploadform, name='uploadform'),    
    url(r'^delete/$', views.delete, name='delete'), 
    url(r'search/', views.search, name='search'),
    url(r'login/$', django_cas_ng.views.login,name='login'),
    url(r'logout/$', django_cas_ng.views.logout,name='logout'),
]