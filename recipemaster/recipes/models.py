import requests
from autoslug import AutoSlugField
from colorfield.fields import ColorField
from django.conf import settings
from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=255)
    color = ColorField()
    slug = AutoSlugField(populate_from='title')

    def __str__(self):
        return self.title


class Recipe(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255, db_index=True)
    html_content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='recipes', blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.url:
            self.html_content = requests.get(self.url).text
        super().save(*args, **kwargs)


class RecipeCollection(models.Model):
    recipes = models.ManyToManyField(Recipe, related_name='collections')
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
