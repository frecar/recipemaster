from django.contrib import admin

# Register your models here.
from .models import Recipe, RecipeCollection

admin.site.register(Recipe)
admin.site.register(RecipeCollection)

