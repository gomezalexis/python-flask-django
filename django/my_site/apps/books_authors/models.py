# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

class Author(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=240)
    books = models.ManyToManyField(Book, related_name="authors")

    def __str__(self):
        the_author = "{}, {}".format(self.last_name, self.first_name)
        return the_author
