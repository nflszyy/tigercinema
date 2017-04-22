# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.conf import settings

from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm
from moviepy.editor import *
import os

movie_count=1

def homepage(request):

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'myapp/homepage.html',
        {'documents': documents}
    )
def feedback(request):
    return render(request,'myapp/feedback.html')

def welcome(request):
    return render(request, 'myapp/welcome.html')

def uploadform(request):
    global movie_count
    if request.method == 'POST':

        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            movie_count+=1
            firstname = form.cleaned_data['fname']
            lastname = form.cleaned_data['lname']
            descript = form.cleaned_data['description']
            titlename = form.cleaned_data['title']
            thumb = lastname+str(movie_count)+'.jpg'
            newdoc = Document(fname = firstname, lname = lastname, title = titlename, thumbnail = thumb, description = descript, docfile=request.FILES['docfile'])         
            #need to figure out how to handle data from choice
            #here is where we put this data on some database      
            newdoc.save()

            path = os.path.join(settings.BASE_DIR, 'myproject', 'myapp', 'static', 'thumbnails')  
            clip = VideoFileClip(os.path.join(settings.MEDIA_ROOT, newdoc.docfile.name))
            thumb_path = os.path.join(path, thumb)

            clip.save_frame(thumb_path, t=0.50)

            # Redirect to the document list after POST
            return HttpResponseRedirect('myapp/uploadsuccess')
    else:
        form = DocumentForm()  # A empty, unbound form

        # Load documents for the list page
        #documents = Document.objects.all()

    return render(
        request, 'myapp/uploadform.html',
        { 'form':form}
        )

def uploadsuccess(request):
    return render(request, 'myapp/uploadsuccess.html')

def documentary(request):
 # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'myapp/documentary.html',
        {'documents': documents}
    )
def narrative(request):
 # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'myapp/narrative.html',
        {'documents': documents}
    )


# http://stackoverflow.com/questions/20205137/how-to-delete-files-in-django
def delete(request):
    if request.method != 'POST':
        raise Http404
    docId = request.POST.get('docfile', None)
    docToDel = get_object_or_404(Document, pk = docId)
    docToDel.docfile.delete()
    docToDel.delete()
    return HttpResponseRedirect('http://127.0.0.1:8000/myapp/homepage/')


