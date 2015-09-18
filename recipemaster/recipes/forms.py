from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from recipemaster.recipes.models import Recipe, RecipeCollection
from django import forms


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'url', 'tags']

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['tags'].help_text = None


class CollectionForm(ModelForm):
    class Meta:
        model = RecipeCollection
        fields = ['title']


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None

        self.fields['password2'].help_text = None


class AddUserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=100,
        label='',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Search for recipes'})
    )
