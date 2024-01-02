# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..bill.bill import Bill
# Create your models here.
# api/models.py

class Vote(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='votes')

    def __str__(self):
        return f"Vote for {self.bill}"
