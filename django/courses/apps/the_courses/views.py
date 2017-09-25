# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render,redirect
from models import Course, Description, CourseManager

def index(request):
    context = {
        'levels' : Description.objects.all(),
        'courses' : Course.objects.all(),
    }
    return render(request, 'the_courses/index.html', context)

def add_course(request):
    if request.method == 'POST':
        errors = Course.objects.basic_validator(request.POST)
        if len(errors) != 0:
            for error in errors:
                messages.error(request, error)
            return redirect(index)
        else:
            Course.objects.create(name=request.POST['name'],the_level=Description.objects.get(id=int(request.POST['the_level'])))
            return redirect('/the_courses')
    else:
        return redirect(index)

def show_desc(request, id):
    return render(request, 'the_courses/show_desc.html', {'description': Description.objects.get(id=id)})

def destroy(request, id):
    return render(request, 'the_courses/destroy.html', {'course': Course.objects.get(id=id)})

def delete(request, id):
    if request.method == "POST":
        bye_user = Course.objects.get(id=id)
        bye_user.delete()
        return redirect(index)
