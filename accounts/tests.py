from django.test import TestCase

# Create your tests here.

from .models import Movie

class AnimalTestCase(TestCase):
    def setUp(self):
            print("setUp: Run once for every test method to setup clean data.")
            pass
    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)