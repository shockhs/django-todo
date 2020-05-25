# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default = False)
    username = models.CharField(max_length=40,default='defaultname')
    
    def __str__ (self):
        return self.text
