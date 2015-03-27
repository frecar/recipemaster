from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from recipemaster.recipes.forms import RecipeForm
from recipemaster.recipes.models import Recipe, Tag


def index(request):
    recipes = Recipe.objects.order_by('-id')
    context = {'recipes': recipes}
    return render(request, 'recipes/index.html', context)


def tag_filter(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    recipes = Recipe.objects.filter(tags=tag).order_by('id')
    context = {'recipes': recipes}
    return render(request, 'recipes/index.html', context)


def add_recipe(request):
    form = RecipeForm()
    if request.POST:
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Added recipe")
            return redirect('recipes:index')
    return render(request, 'recipes/add_recipe.html', {
        'form': form
    })
