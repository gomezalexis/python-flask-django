# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Dojo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    desc = models.TextField()

    def __str__(self):
        the_dojo = "{}, {} {}".format(self.name, self.city, self.state)
        return the_dojo

class Ninja(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # foreign key for one to many. There can be a lot of ninjas
    # in a dojo
    dojo = models.ForeignKey(Dojo, related_name="ninjas")

    def __str__(self):
        the_ninja = "{} {}".format(self.first_name, self.last_name)
        return the_ninja

# Create your models here.
