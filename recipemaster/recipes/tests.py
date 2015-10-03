from unittest import mock

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase

from recipemaster.recipes.models import Recipe, RecipeCollection, Tag


class CreateUserMixin(object):
    def setUp(self):
        self.user = User.objects.create_user('datusername', password='datpassword')
        self.client.login(username='datusername', password='datpassword')


class SmokeTestCase(CreateUserMixin, TestCase):

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


class EditCollectionTest(CreateUserMixin, TestCase):

    def test_add_collection_should_render_form(self):
        response = self.client.get(reverse('recipes:add_collection'))
        self.assertContains(response, 'Create collection')
        self.assertContains(response, '<form method="post">')

    def test_add_collection_should_create_collection(self):
        response = self.client.post(reverse('recipes:add_collection'), {'title': 'Dinners'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(RecipeCollection.objects.last().title, 'Dinners')

    def test_edit_collection_should_render_form(self):
        collection = RecipeCollection.objects.create(title='super collection')
        collection.users.add(self.user)
        response = self.client.get(reverse('recipes:edit_collection', args=[collection.pk]))
        self.assertContains(response, 'Edit collection')
        self.assertContains(response, '<form method="post">')

    def test_edit_collection_should_create_edited_collection(self):
        collection = RecipeCollection.objects.create(title='super collection')
        collection.users.add(self.user)
        response = self.client.post(
            reverse('recipes:edit_collection', args=[collection.pk]),
            {'title': 'Desserts'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(RecipeCollection.objects.last().title, 'Desserts')


class DeleteCollectionTest(CreateUserMixin, TestCase):

    def test_delete_collection_should_remove_collection(self):
        collection = RecipeCollection.objects.create(title='super collection')
        collection.users.add(self.user)
        response = self.client.post(
            reverse('recipes:delete_collection', args=[collection.pk]),
            {'delete': 'yes'})
        self.assertEqual(response.status_code, 302)
        self.assertFalse(RecipeCollection.objects.filter(pk=collection.id).exists())

    def test_delete_collection_should_not_delete_getrequests(self):
        collection = RecipeCollection.objects.create(title='super collection')
        collection.users.add(self.user)
        response = self.client.get(
            reverse('recipes:delete_collection', args=[collection.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(RecipeCollection.objects.filter(pk=collection.id).exists())
