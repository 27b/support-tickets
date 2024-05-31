import json

from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.test import APIClient


class AccountTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.username = 'test'
        self.password = '1234'
        User.objects.create_user(
            username=self.username,
            password=self.password
        ).save()

    def test_user_creation(self):
        users = User.objects.all()
        count = len(users)
        self.assertEqual(count, 1)
    
    def test_api_account_login(self):
        payload = {'username': self.username, 'password': self.password}
        request = self.client.post("/auth/signin", payload)
        content = json.loads(request.content)
        self.assertIsNotNone(content.get('token'))