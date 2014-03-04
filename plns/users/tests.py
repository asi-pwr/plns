from django.test import TestCase

from plns.users.models import User


# Create your tests here.

class UserTests(TestCase):
    def setUp(self):
        self.email = 'user@domena.com'
        self.password = 'haslo'

    def test_can_create_user(self):
        testuser = User.objects.create_user(self.email, self.password)
        self.assertTrue(User.objects.filter(email=self.email).exists())





