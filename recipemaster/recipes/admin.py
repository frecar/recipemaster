from django.contrib import admin

# Register your models here.
from .models import Recipe, RecipeCollection


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeCollection)
