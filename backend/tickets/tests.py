import json

from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.test import APIClient

from .models import Ticket


class TitcketTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        user1 = User.objects.create_user(username='test1', password='1234')
        user2 = User.objects.create_user(username='test2', password='1234')

        user1.save()
        user2.save()
    
        payload = {'username': 'test1', 'password': '1234'}
        request = self.client.post("/auth/signin", payload)
        content = json.loads(request.content)

        self.token = content.get('token')

        self.ticket = Ticket.objects.create(
            title='Awesome Title',
            description='Awesome description',
            user=user1)
        
        self.ticket.save()

    def test_api_ticket_list(self):
        request = self.client.get("/tickets", HTTP_AUTHORIZATION=self.token)
        content = json.loads(request.content)
        
        self.assertEqual(content[0].get('id'), self.ticket.id)
        self.assertEqual(content[0].get('title'), self.ticket.title)
        self.assertEqual(content[0].get('description'), self.ticket.description)
        self.assertEqual(content[0].get('comment'), [])

    def test_api_ticket_create_and_retrieve(self):
        payload = {'title': 'alice in the wonderland', 'description': 'Comming Soon...'}
        request = self.client.post("/tickets", payload, HTTP_AUTHORIZATION=self.token)
        content = json.loads(request.content)

        self.assertEqual(content.get('id'), 2)
        self.assertEqual(content.get('title'), 'alice in the wonderland')
        self.assertEqual(content.get('description'), 'Comming Soon...')
        self.assertEqual(content.get('account').get('id'), 1)
        self.assertEqual(content.get('account').get('username'), 'test1')
        self.assertEqual(content.get('comment'), [])
    
        request = self.client.get("/tickets/2", HTTP_AUTHORIZATION=self.token)
        content = json.loads(request.content)

        self.assertEqual(content.get('id'), 2)
        self.assertEqual(content.get('title'), 'alice in the wonderland')

    def test_api_ticket_update(self):
        payload = {'title': 'posesiones', 'description': 'Comming Soon...'}
        request = self.client.post("/tickets", payload, HTTP_AUTHORIZATION=self.token)
        content = json.loads(request.content)
        id = content.get('id')

        self.assertEqual(content.get('title'), 'posesiones')
        
        payload = {'title': 'godzilla and kong', 'description': content.get('description')}
        request = self.client.put("/tickets/" + str(id), payload, HTTP_AUTHORIZATION=self.token)
        content = json.loads(request.content)

        self.assertEqual(content.get('id'), id)
        self.assertEqual(content.get('title'), 'godzilla and kong')
