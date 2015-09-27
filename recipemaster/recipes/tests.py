from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from recipemaster.recipes.models import RecipeCollection, Tag, Recipe
from unittest import mock


class SmokeTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('datusername', password='datpassword')
        self.client.login(username='datusername', password='datpassword')

    def test_index(self):
        response = self.client.get(reverse('recipes:index'))
        self.assertContains(response, 'Recipe collector', status_code=200)

    def test_view_collection(self):
        collection = RecipeCollection.objects.create(title='super collection')
        collection.users.add(self.user)
        response = self.client.get(reverse('recipes:view_collection', args=[collection.pk]))
        self.assertContains(response, 'super collection')

    @mock.patch('requests.get')
    def test_tag_filter(self, mock_get):
        collection = RecipeCollection.objects.create(title='super collection')
        collection.users.add(self.user)
        tag = Tag.objects.create(title='fish')
        recipe = Recipe.objects.create(title='dinner')
        recipe.tags.add(tag)
        collection.recipes.add(recipe)
        response = self.client.get(reverse('recipes:tag_filter', args=[collection.pk, tag.slug]))
        self.assertContains(response, 'super collection')
        self.assertContains(response, 'fish')
