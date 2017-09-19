# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    request.session['counter'] += 1

    context = {
        "word" : get_random_string(length=14),
    }
    return render(request,'random_word/main.html', context)

def reset(request):
    request.session['counter'] = 0

    return redirect(index)