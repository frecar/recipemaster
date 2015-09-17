from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from recipemaster.recipes.forms import RecipeForm, CollectionForm, SearchForm
from recipemaster.recipes.models import Recipe, Tag, RecipeCollection
from .forms import AddUserForm


@login_required
def index(request):
    collections = RecipeCollection.objects.filter(users=request.user).order_by('title')
    return render(request, 'recipes/index.html', {'collections': collections})


def tag_filter(request, collection_id, slug):
    collection = get_object_or_404(RecipeCollection, pk=collection_id, users=request.user)
    tag = get_object_or_404(Tag, slug=slug)
    recipes = collection.recipes.filter(tags=tag).order_by('id')
    return render(request, 'recipes/view_collection.html', {
        'collection': collection,
        'recipes': recipes
    })


@staff_member_required
def edit_recipe(request, recipe_id=None):
    recipe = Recipe()
    if recipe_id:
        recipe = get_object_or_404(Recipe, pk=recipe_id, collections__users=request.user)
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


@login_required
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


@login_required
def delete_collection(request, collection_id):
    collection = get_object_or_404(RecipeCollection, pk=collection_id, users=request.user)
    if request.POST:
        if request.POST.get('delete') == 'yes':
            collection.delete()
            messages.success(request, 'Deleted collection')
        else:
            messages.error(request, 'Could not delete collection. Try again. ')
    return redirect('recipes:index')


@login_required
def view_collection(request, collection_id):
    collection = get_object_or_404(RecipeCollection, pk=collection_id, users=request.user)
    recipes = collection.recipes.all()
    form = SearchForm()
    if request.POST:
        form = SearchForm(request.POST)
        if form.is_valid:
            print(request.POST)
            recipes = collection.recipes.filter(title__icontains=request.POST.get(key='search'))
            return render(request, 'recipes/view_collection.html', {
                'collection': collection,
                'form': form,
                'recipes': recipes
            })
        else:
            messages.error(request, 'Could not search. Please try again.')
    return render(request, 'recipes/view_collection.html', {
        'collection': collection,
        'form': form,
        'recipes': recipes
    })


@login_required
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


@login_required
def edit_recipe_in_collection(request, collection_id, recipe_id=None):
    collection = get_object_or_404(RecipeCollection, pk=collection_id, users=request.user)
    recipe = Recipe()
    if recipe_id:
        recipe = get_object_or_404(Recipe, pk=recipe_id)
    form = RecipeForm(instance=recipe)
    if request.POST:
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save()
            collection.recipes.add(recipe)
            messages.success(request, 'Saved recipe')
            return redirect('recipes:view_collection', collection_id=collection.pk)
    return render(request, 'recipes/edit_recipe.html', {
        'form': form
    })


@login_required
def add_user_to_collection(request, collection_id):
    collection = get_object_or_404(RecipeCollection, pk=collection_id, users=request.user)
    form = AddUserForm()
    if request.POST:
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data['username'])
            collection.users.add(user)
            messages.success(request, 'User added to collection')
            return redirect('recipes:view_collection', collection_id=collection.pk)
        else:
            messages.error(request, 'Could not add user. Please try again.')
    return render(request, 'recipes/add_user_to_collection.html', {
        'form': form, 'collection': collection})
