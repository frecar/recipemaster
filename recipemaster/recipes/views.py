from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
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


@staff_member_required
def edit_recipe(request, recipe_id=None):
    recipe = Recipe()
    if recipe_id:
        recipe = get_object_or_404(Recipe, pk=recipe_id)
    form = RecipeForm(instance=recipe)
    if request.POST:
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved recipe')
            return redirect('recipes:index')
    return render(request, 'recipes/edit_recipe.html', {
        'form': form
    })
