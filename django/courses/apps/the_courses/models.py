# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Description(models.Model):
    level = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.level

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = []
        if len(postData['name']) < 6:
            errors.append("Course name should be more than 5 characters")
        return errors

class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    the_level = models.ForeignKey(Description, related_name='courses')

    objects = CourseManager()
    def __str__(self):
        return self.name


