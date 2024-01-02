# api/tests/test_models.py

from django.test import TestCase
from ..legislator.legislator import Legislator
from ..bill.bill import Bill
from ..vote.vote import Vote
from ..person.person import Person
from .vote_result import VoteResult

class VoteResultModelTest(TestCase):
    def setUp(self):
        # Create a Legislator instance
        self.legislator = Legislator.objects.create(name='John Doe')

        # Create a Bill instance
        primary_sponsor= Person.objects.create(name='John Doe')
        self.bill = Bill.objects.create(title='Sample Bill', primary_sponsor=primary_sponsor)

        # Create a Vote instance
        self.vote = Vote.objects.create(bill=self.bill)

    def test_create_vote_result(self):
        # Create a VoteResult instance
        vote_result = VoteResult.objects.create(
            legislator=self.legislator,
            vote=self.vote,
            vote_type=1  # 1 for yea, 2 for nay
        )

        # Retrieve the saved VoteResult instance from the database
        saved_vote_result = VoteResult.objects.get(id=vote_result.id)

        # Check if the data matches the expected values
        self.assertEqual(saved_vote_result.legislator, self.legislator)
        self.assertEqual(saved_vote_result.vote, self.vote)
        self.assertEqual(saved_vote_result.vote_type, 1)

    def test_str_method(self):
        # Create a VoteResult instance
        vote_result = VoteResult.objects.create(
            legislator=self.legislator,
            vote=self.vote,
            vote_type=1
        )

        # Check the __str__ method
        self.assertEqual(str(vote_result), f"{self.legislator.name} voted yea on {self.vote.bill.title}")
