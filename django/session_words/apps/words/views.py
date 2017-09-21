# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,redirect
from time import strftime,gmtime

# Create your views here.
def index(request):
    if 'all_words' not in request.session:
        request.session['all_words'] = []

    print request.session['all_words']
    return render(request, 'words/index.html')

def add_word(request):
    if request.method == "POST":
        if not 'bold' in request.POST:  #request.POST['bold']
            request.session['bold'] = "style=font-size:16px"

        else:
            request.session['bold'] = request.POST['bold']

        new_word = {
            "word": request.POST['word'],
            "color": request.POST['color'],
            "bold": request.session['bold'],
            "time": strftime("%b %d, %Y %I:%M %p")
        }   
        #attaching the words to the array initiated in index
        request.session['all_words'].append(new_word)
    print request.session['color']
    return redirect('/')

def clear(request):
    request.session['all_words'] = []
    return redirect('/')
