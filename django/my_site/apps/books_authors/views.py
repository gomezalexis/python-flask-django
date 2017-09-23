# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Book

def index(request):
    books = Book.objects.all()
    return render(request,'books_authors/index.html',{'books':books})