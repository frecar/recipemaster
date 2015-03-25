from django.contrib import admin

# Register your models here.
from .models import Recipe, RecipeCollection, Tag


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeCollection)
admin.site.register(Tag)
