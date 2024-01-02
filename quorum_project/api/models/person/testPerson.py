# api/tests/test_models.py

from django.test import TestCase
from .person import Person

class PersonModelTest(TestCase):
    def test_create_person(self):
        # Create a Person instance
        person = Person.objects.create(name='John Doe')

        # Retrieve the saved Person instance from the database
        saved_person = Person.objects.get(id=person.id)

        # Check if the data matches the expected values
        self.assertEqual(saved_person.name, 'John Doe')

    def test_str_method(self):
        # Create a Person instance
        person = Person.objects.create(name='Jane Doe')

        # Check the __str__ method
        self.assertEqual(str(person), 'Jane Doe')
