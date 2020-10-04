from rest_framework.test import APITestCase, APIClient
from django.utils import timezone

from api.models import Mem


class TestMemberDetailView(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_members(self):
        now = timezone.now()
        Mem.objects.create(name='Jhon Doe', phone='123456', position='Senior Developer', dob=now,
                           vertical='Test', department='TestDepartment')

        response = self.client.get('/api/members/')

        self.assertEqual(200, response.status_code, str(response.content))
        self.assertEqual(response.json()[0]['name'], 'Jhon Doe')

    def test_retrieve_members(self):
        now = timezone.now()
        mem = Mem.objects.create(name='Jhon Doe', phone='123456', position='Senior Developer', dob=now,
                                 vertical='Test', department='TestDepartment')

        response = self.client.get(f'/api/members/{mem.id}/')

        self.assertEqual(200, response.status_code, str(response.content))
        self.assertEqual(response.json()['name'], 'Jhon Doe')
