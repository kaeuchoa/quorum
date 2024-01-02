# api/serializers.py

from rest_framework import serializers
# api/serializers.py
from .models.person.person import Person
from .models.bill.bill import Bill
from .models.legislator.legislator import Legislator
from .models.vote.vote import Vote
from .models.vote_result.vote_result import VoteResult


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    primary_sponsor = PersonSerializer()

    class Meta:
        model = Bill
        fields = '__all__'

class LegislatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Legislator
        fields = '__all__'

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'

class VoteResultSerializer(serializers.ModelSerializer):
    legislator = LegislatorSerializer()

    class Meta:
        model = VoteResult
        fields = '__all__'
