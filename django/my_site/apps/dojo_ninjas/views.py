# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Dojo


# Create your views here.
def index(request):
    dojos = Dojo.objects.order_by("city")
    return render(request,'dojo_ninjas/index.html',{'dojos': dojos})
