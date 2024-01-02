# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# api/models.py

class Legislator(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
