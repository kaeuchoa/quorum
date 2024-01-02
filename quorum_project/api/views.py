# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets
from .models.person.person import Person
from .models.bill.bill import Bill
from .models.legislator.legislator import Legislator
from .models.vote.vote import Vote
from .models.vote_result.vote_result import VoteResult
from .serializers import BillSerializer, LegislatorSerializer, VoteSerializer, VoteResultSerializer

# api/views.py
class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class LegislatorViewSet(viewsets.ModelViewSet):
    queryset = Legislator.objects.all()
    serializer_class = LegislatorSerializer

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

class VoteResultViewSet(viewsets.ModelViewSet):
    queryset = VoteResult.objects.all()
    serializer_class = VoteResultSerializer
