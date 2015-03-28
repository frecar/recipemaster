from django.forms import ModelForm
from recipemaster.recipes.models import Recipe


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'url', 'tags']

    def __init__(self):
        super().__init__()
        self.fields['tags'].help_text = None
