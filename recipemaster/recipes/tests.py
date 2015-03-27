from django.core.urlresolvers import reverse
from django.test import TestCase
from recipemaster.recipes.models import Tag


class SmokeTestCase(TestCase):
    def test_index(self):
        response = self.client.get(reverse('recipes:index'))
        self.assertContains(response, 'Recipemaster')

    def test_tag_filter(self):
        tag = Tag.objects.create(title='Cake')
        response = self.client.get(reverse('recipes:tag_filter', args=[tag.slug]))
        self.assertContains(response, 'Recipemaster')
