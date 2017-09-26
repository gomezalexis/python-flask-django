# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
NAMES_REGEX = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = []
        if len(postData['first_name']) < 3 or len(postData['last_name']) < 3:
            errors.append("Name and Last Name needs to be longer that 2 characters")
        if not NAMES_REGEX.match(postData['first_name']) or not NAMES_REGEX.match(postData['last_name']):
            errors.append("Name and Last Name should only contain letters")
        if not EMAIL_REGEX.match(postData['email']):
            errors.append("Invalid email format")
        if postData['pass_confirm'] != postData['password']:
            errors.append("Password doesn't match")
        return errors
            

class User(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)
    login_times = models.IntegerField(default=0)
    # pass_confir = models.CharField(max_length=100)
    objects = UserManager()

    def __str__(self):
        in_string = "{}, {}".format(self.last_name, self.first_name)
        return in_string
    