# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..person.person import Person

# Create your models here.
# api/models.py

class Bill(models.Model):
    title = models.CharField(max_length=255)
    primary_sponsor = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='sponsored_bills')

    def __str__(self):
        return f"{self.title}"
