from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from recipemaster.recipes.models import Recipe, RecipeCollection


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'url', 'tags']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].help_text = None


class CollectionForm(ModelForm):
    class Meta:
        model = RecipeCollection
        fields = ['title']


class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password2'].help_text = None
