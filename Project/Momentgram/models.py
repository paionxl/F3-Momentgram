# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser

'''
User in Django by deafault have the following primary attributes:

    - username
    - mail
    - password
    - first name
    - last name

That's why I propose the following extension of the Django class AbstractUser that will allow us to
save extra information to our usersgit  
'''


class User(AbstractUser):
    phone_number = models.PositiveIntegerField(max_length=9, blank=True, unique=True)
    bio = models.TextField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    web_site = models.TextField(max_length=75, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    gender = models.TextField(max_length=20, blank=True)


