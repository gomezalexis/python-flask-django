# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from time import gmtime, strftime

# Create your views here.
def index(request): 
    context = {
    "time": strftime("%b %d, %Y %I:%M %p")  #changed the time in settings TIME_ZONE
    }


    return render(request,'time_str/index.html', context)
