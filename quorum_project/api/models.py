# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# api/models.py

class Person(models.Model):
    name = models.CharField(max_length=255)

class Bill(models.Model):
    title = models.CharField(max_length=255)
    primary_sponsor = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='sponsored_bills')

class Legislator(models.Model):
    name = models.CharField(max_length=255)

class Vote(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='votes')

class VoteResult(models.Model):
    YEA = 1
    NAY = 2
    VOTE_TYPE_CHOICES = [
        (YEA, 'Yea'),
        (NAY, 'Nay'),
    ]

    legislator = models.ForeignKey(Legislator, on_delete=models.CASCADE, related_name='votes_cast')
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE, related_name='vote_results')
    vote_type = models.IntegerField(choices=VOTE_TYPE_CHOICES)
