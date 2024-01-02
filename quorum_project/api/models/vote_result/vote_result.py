# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..legislator.legislator import Legislator
from ..vote.vote import Vote

class VoteResult(models.Model):
    VOTE_TYPE_CHOICES = {1: 'yea', 2: 'nay'} 

    legislator = models.ForeignKey(Legislator, on_delete=models.CASCADE, related_name='votes_cast')
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE, related_name='vote_results')
    vote_type = models.IntegerField(choices=VOTE_TYPE_CHOICES)

    def __str__(self):
        return f"{self.legislator.name} voted {self.VOTE_TYPE_CHOICES[self.vote_type]} on {self.vote.bill.title}"
