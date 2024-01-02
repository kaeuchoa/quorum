# api/tests/test_models.py

from django.test import TestCase
from .bill import Bill
from ..person.person import Person

class BillModelTest(TestCase):
    def setUp(self):
        # Create a Person instance for the primary sponsor
        self.primary_sponsor = Person.objects.create(name='John Doe')

    def test_create_bill(self):
        # Create a Bill instance
        bill = Bill.objects.create(
            title='Sample Bill',
            primary_sponsor=self.primary_sponsor
        )

        # Retrieve the saved Bill instance from the database
        saved_bill = Bill.objects.get(id=bill.id)

        # Check if the data matches the expected values
        self.assertEqual(saved_bill.title, 'Sample Bill')
        self.assertEqual(saved_bill.primary_sponsor, self.primary_sponsor)

    def test_str_method(self):
        # Create a Bill instance
        bill = Bill.objects.create(
            title='Sample Bill',
            primary_sponsor=self.primary_sponsor
        )

        # Check the __str__ method
        self.assertEqual(str(bill), 'Sample Bill')
