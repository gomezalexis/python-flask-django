from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from models import *

def index(request):
    users = User.objects.all()
    return render(request, 'users/index.html',{"users": users})

def new(request):
    return render(request,'users/new.html')

def show(request, id):
    return render(request, 'users/show.html', {"user": User.objects.get(id= id)})

def edit(request, id):
    
    return render(request, 'users/edit.html', {"user": User.objects.get(id= id)})

def delete(request, id):
    if request.method == 'POST':
        destroy_user = User.objects.get(id=id)
        destroy_user.delete()
    return redirect('/users')

def update(request, id):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for error in errors:
                messages.error(request, error)
            return redirect(edit)
        else:
            user_to_update = User.objects.get(id=id)
            user_to_update.full_name = request.POST['full_name']
            user_to_update.email = request.POST['email']     
            user_to_update.save()  
            return redirect('/users')

def create(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for error in errors:
                messages.error(request, error)
            return redirect('users/new')
        else:
            User.objects.create(full_name=request.POST['full_name'], email=request.POST['email'])
            return redirect('/users')
    
    else:
        return redirect('/users/new')
