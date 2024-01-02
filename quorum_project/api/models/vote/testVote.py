# api/tests/test_models.py

from django.test import TestCase
from .vote import Vote
from ..bill.bill import Bill
from ..person.person import Person

class VoteModelTest(TestCase):
    def setUp(self):
        # Create a Bill instance for the vote
        primary_sponsor= Person.objects.create(name='John Doe')
        self.bill = Bill.objects.create(title='Sample Bill', primary_sponsor=primary_sponsor)

    def test_create_vote(self):
        # Create a Vote instance
        vote = Vote.objects.create(bill=self.bill)

        # Retrieve the saved Vote instance from the database
        saved_vote = Vote.objects.get(id=vote.id)

        # Check if the data matches the expected values
        self.assertEqual(saved_vote.bill, self.bill)

    def test_str_method(self):
        # Create a Vote instance
        vote = Vote.objects.create(bill=self.bill)

        # Check the __str__ method
        self.assertEqual(str(vote), f"Vote for {self.bill}")
