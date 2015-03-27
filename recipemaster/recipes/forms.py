from django.forms import ModelForm
from recipemaster.recipes.models import Recipe


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'url']


