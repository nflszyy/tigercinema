
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import imageio
imageio.plugins.ffmpeg.download()
from moviepy.editor import *
import os
import functools
import operator
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating
from urllib.request import urlopen
movie_count = 1

# View function for homepage
@login_required(login_url='/accounts/login/',redirect_field_name='/myapp/homepage/')
def homepage(request):
    user=request.user
    netid=user.username
    # Load documents for the list page
    documents = Document.objects.all()
    rateddocuments = Document.objects.filter(ratings__isnull=False).order_by('ratings__average').reverse()[0:4]

    # Render list page with the documents and the form
    return render(
        request,
        'myapp/homepage.html',
        {'documents': documents, 'rateddocuments': rateddocuments, 'netid':netid}
    )

# View function for feedback
@login_required(login_url='/accounts/login/',redirect_field_name='/myapp/homepage/')
def feedback(request):
    user=request.user
    netid=user.username
    return render(request,'myapp/feedback.html',{'netid':netid})

# View function for welcome page
def welcome(request):
    return render(request, 'myapp/welcome.html')

# View Function for uploadform
@login_required(login_url='/accounts/login/',redirect_field_name='/myapp/homepage/')
def uploadform(request):
    user=request.user
    netid=user.username
    global movie_count
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            user=request.user
            movie_count+=1
            firstname = form.cleaned_data['fname']
            lastname = form.cleaned_data['lname']
            descript = form.cleaned_data['description']
            titlename = form.cleaned_data['title']
            choiceval = form.cleaned_data['choice']
            url = form.cleaned_data['docfile']
            thumb = form.cleaned_data['thumbnail']
            punetid = user.username
            newdoc = Document(fname = firstname, lname = lastname, title = titlename, 
                              thumbnail = thumb, description = descript, 
                              choice = choiceval, docfile=url, netid = punetid)

            newdoc.save()
            # Redirect to the document list after POST
            return HttpResponseRedirect('/myapp/homepage/')
    else:
        form = DocumentForm()  # A empty, unbound form

        # Load documents for the list page
        #documents = Document.objects.all()

    return render(
        request, 'myapp/uploadform.html',
        { 'form':form, 'netid':netid}
        )
# View Function for Documentaries
@login_required(login_url='/accounts/login/',redirect_field_name='/myapp/homepage/')
def documentary(request):
 # Load documents for the list page
    # Get all the films in the documentary category
    documents = Document.objects.filter(choice__exact='2')
    user=request.user
    netid=user.username

    # Render list page with the documents and the form
    return render(
        request,
        'myapp/documentary.html',
        {'documents': documents,'netid':netid}
    )

# View Function for Narratives
@login_required(login_url='/accounts/login/',redirect_field_name='/myapp/homepage/')
def narrative(request):
 # Load documents for the list page
    # Get all the films in the narrative category
    documents = Document.objects.filter(choice__exact='1')
    user=request.user
    netid=user.username

    # Render list page with the documents and the form
    return render(
        request,
        'myapp/narrative.html',
        {'documents': documents,'netid':netid}
    )

# Function to delete things
# http://stackoverflow.com/questions/20205137/how-to-delete-files-in-django
@login_required(login_url='/accounts/login/',redirect_field_name='/myapp/homepage/')
def delete(request):
    global movie_count
    if request.method != 'POST':
        raise Http404
    docId = request.POST.get('docfile', None)
    docToDel = get_object_or_404(Document, pk = docId)
    #docToDel.docfile.delete()
    movie_count -= 1
    docToDel.delete()
    return HttpResponseRedirect('/myapp/homepage/')

# Function to Search for films by title or by filmmaker
@login_required(login_url='/accounts/login/',redirect_field_name='/myapp/homepage/')
def search(request):

    if request.method == 'GET':
        user=request.user
        netid=user.username
        query = request.GET.get('search', None)
        if query:
            query_list = query.split()
            documents = Document.objects.filter(
                functools.reduce(operator.or_, 
                                (Q(fname__icontains=q) for q in query_list)) |
                functools.reduce(operator.or_, 
                                (Q(lname__icontains=q) for q in query_list)) |
                functools.reduce(operator.or_, 
                                (Q(title__icontains=q) for q in query_list))
                )
            return render(
                    request,
                    'myapp/searchlistings.html',
                    {'documents': documents,'netid':netid}
            )
        else: return HttpResponseRedirect('/myapp/homepage/')

# Play the film clicked by the user, the film is identified by the primary key in the database
@login_required(login_url='/accounts/login/',redirect_field_name='/myapp/homepage/')
def play(request, user_id):
    user=request.user
    netid=user.username
    video = Document.objects.get(pk=user_id)
    rateddocuments = Document.objects.filter(ratings__isnull=False).order_by('ratings__average').reverse()[0:4]
    return render(request, 'myapp/play.html', {'videos': video, 'rateddocuments':rateddocuments, 'netid':netid})

# Display all films uploaded by a particular filmmaker
@login_required(login_url='/accounts/login/',redirect_field_name='/myapp/homepage/')
def mymovies(request):
    user=request.user
    netid=user.username
    documents = Document.objects.filter(netid=netid)
    return render(request, 'myapp/mymovies.html', {'documents': documents,'netid':netid})




