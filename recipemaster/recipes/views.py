from django.shortcuts import render, get_object_or_404
from recipemaster.recipes.models import Recipe
# Create your views here.


def index(request):
    latest_recipe_list = Recipe.objects.order_by('-id')[:5]
    context = {'latest_recipe_list': latest_recipe_list}
    return render(request, 'recipes/index.html', context)


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/details.html', {'recipe': recipe})
