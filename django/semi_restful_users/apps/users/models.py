# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['full_name']) < 5:
            errors['full_name'] = "The Full name should be longer that 5 characters"
        if len(postData['email']) < 7:
            errors['email'] = "The email needs to be longer that 7 characters"
        return errors

class User(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)

    objects = UserManager()

    def __str__(self):
        return self.full_name
