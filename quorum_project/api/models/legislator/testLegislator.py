# api/tests/test_models.py

from django.test import TestCase
from .legislator import Legislator

class LegislatorModelTest(TestCase):
    def test_create_legislator(self):
        # Create a Legislator instance
        legislator = Legislator.objects.create(name='John Doe')

        # Retrieve the saved Legislator instance from the database
        saved_legislator = Legislator.objects.get(id=legislator.id)

        # Check if the data matches the expected values
        self.assertEqual(saved_legislator.name, 'John Doe')

    def test_str_method(self):
        # Create a Legislator instance
        legislator = Legislator.objects.create(name='Jane Doe')

        # Check the __str__ method
        self.assertEqual(str(legislator), 'Jane Doe')
