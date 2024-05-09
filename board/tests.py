from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from .models import Task, Board


class CreateTaskTest(APITestCase):
    def setUp(self):
        # Benutzer und Token erstellen
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        # Den Authorization Header für alle Testanfragen einstellen
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        # Erstellen einer Board-Instanz, wenn notwendig
        self.board = Board.objects.create(name='Test Board')
        self.task_data = {
            'title': 'Test Task',
            'description': 'Test Task Description',
            'user': self.user.id,
            'board': self.board.id,
            'status': 'todo',  # Optional, da es einen Default-Wert gibt
        }
    def test_create_task(self):
        response = self.client.post("/createTask/",self.task_data, format='json')
        self.assertEqual(response.status_code, 201)
