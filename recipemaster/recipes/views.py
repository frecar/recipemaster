from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from recipemaster.recipes.forms import RecipeForm, CollectionForm
from recipemaster.recipes.models import Recipe, Tag, RecipeCollection


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


@staff_member_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.POST:
        if request.POST.get('delete') == 'yes':
            recipe.delete()
            messages.success(request, 'Deleted recipe')
        else:
            messages.error(request, 'Could not delete recipe. Try again. ')
    return redirect('recipes:index')


@staff_member_required
def edit_collection(request, collection_id=None):
    collection = RecipeCollection()
    if collection_id:
        collection = get_object_or_404(RecipeCollection, pk=collection_id, users=request.user)
    form = CollectionForm(instance=collection)
    if request.POST:
        form = CollectionForm(request.POST, instance=collection)
        if form.is_valid():
            collection = form.save()
            collection.users.add(request.user)
            messages.success(request, 'Saved collection')
            return redirect('recipes:view_collection', collection_id=collection.pk)
    return render(request, 'recipes/edit_collection.html', {
        'form': form
    })


def view_collection(request, collection_id):
    collection = get_object_or_404(RecipeCollection, pk=collection_id, users=request.user)
    return render(request, 'recipes/view_collection.html', {'collection': collection})


def remove_recipe_from_collection(request, collection_id, recipe_id):
    collection = get_object_or_404(RecipeCollection, pk=collection_id, users=request.user)
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.POST:
        if request.POST.get('delete') == 'yes':
            collection.recipes.remove(recipe)
            messages.success(request, 'Removed recipe from {}'.format(collection.title))
        else:
            messages.error(request, 'Could not delete recipe. Try again. ')
    return redirect('recipes:view_collection', collection_id=collection.pk)
