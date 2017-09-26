# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from models import User, UserManager
import bcrypt

def index(request):
    return render(request, 'registro/index.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for error in errors:
                messages.error(request, error)
            return redirect(index)
        else:
            # Using bcrypt
            hashed_password = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt())
            # creating and adding user
            User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],
            email=request.POST['email'], password=hashed_password)
            
            # taking info of the user
            user = User.objects.get(email=request.POST['email'])
            request.session['the_user'] = user.id

            return redirect(success)
    
    else:
        return redirect(index)

def login(request):
    if request.method == 'POST':
        #filter the users
        user = User.objects.filter(email=request.POST['email'])

        if user: #if user exist in database
            user = User.objects.get(email=request.POST['email'])
            # need to verify the encoded input with the encoded password in database
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['the_user'] = user.id 
                return redirect(success)
            else:
                messages.error(request, "Password is incorrect")
                return redirect(index)
        else:
            messages.error(request, "Email doesn't exist")
            return redirect(index)
    else:
        return redirect(index)
            

def success(request):
    welcome=""
    # attaching the user we want to display
    user = User.objects.get(id=request.session['the_user'])
    # send the user to success
    if user.login_times == 0:
        welcome="Hello new User! {}".format(user.first_name)
        user.login_times += 1
        user.save()
    else:
        welcome="Welcome back {}".format(user)
        user.login_times += 1
        user.save()
      
    return render(request, 'registro/success.html', {'welcome':welcome,'user': user})

