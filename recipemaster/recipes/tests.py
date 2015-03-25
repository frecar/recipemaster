from django.core.urlresolvers import reverse
from django.test import TestCase


class SmokeTestCase(TestCase):
    def test_index(self):
        response = self.client.get(reverse('recipes:index'))
        self.assertContains(response, 'Recipemaster')
