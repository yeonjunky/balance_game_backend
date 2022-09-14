from django.test import TestCase
# from django.contrib.
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token


# Create your tests here.
class UserTest(TestCase):
    # def setUp(self) -> None:
    #     user = User.objects.create()

    def test_sign_up(self):
        username = 'asdf'
        email = 'test@example.com'
        password = '1234'

        created_user = User.objects.create_user(username=username, email=email, password=password)

        user = User.objects.get(pk=created_user.id)

        self.assertEqual(created_user.username, user.username)
        self.assertEqual(created_user.email, user.email)
        self.assertEqual(created_user.password, user.password)

