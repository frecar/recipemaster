from django.shortcuts import render
from recipemaster.recipes.models import Recipe
# Create your views here.


def index(request):
    latest_recipe_list = Recipe.objects.order_by('-id')
    context = {'latest_recipe_list': latest_recipe_list}
    return render(request, 'recipes/index.html', context)
