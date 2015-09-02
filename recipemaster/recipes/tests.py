from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase


class SmokeTestCase(TestCase):

    def setUp(self):
        User.objects.create_user('datusername', password='datpassword')
        self.client.login(username='datusername', password='datpassword')

    def test_index(self):
        response = self.client.get(reverse('recipes:index'))
        self.assertContains(response, 'Recipe collector')
