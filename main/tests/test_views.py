from django.test import TestCase

from main.models import Medicine


class TestStore(TestCase):
    def setUp(self):
        self.medicine = Medicine.objects.create(name='Medicine1')

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    def test_store(self):
        response = self.client.get('/store/')
        self.assertEqual(response.status_code, 200)
