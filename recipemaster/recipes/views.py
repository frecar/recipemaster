from django.shortcuts import render, get_object_or_404
from recipemaster.recipes.models import Recipe, Tag
# Create your views here.


def index(request):
    recipes = Recipe.objects.order_by('-id')
    context = {'recipes': recipes}
    return render(request, 'recipes/index.html', context)


def tag_filter(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    recipes = Recipe.objects.filter(tags=tag).order_by('id')
    context = {'recipes': recipes}
    return render(request, 'recipes/index.html', context)
