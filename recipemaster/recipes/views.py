from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect, render

from recipemaster.recipes.forms import CollectionForm, RecipeForm, SearchForm
from recipemaster.recipes.models import Recipe, RecipeCollection, Tag
from recipemaster.recipes.search import get_query

from .forms import AddUserForm


@login_required
def index(request):
    collections = RecipeCollection.objects.filter(users=request.user).order_by('title')
    return render(request, 'recipes/index.html', {'collections': collections})


@login_required
def tag_filter(request, collection_id, slug):
    collection = get_object_or_404(RecipeCollection, pk=collection_id, users=request.user)
    tag = get_object_or_404(Tag, slug=slug)
    recipes = collection.recipes.filter(tags=tag).order_by('title')
    form = SearchForm()
    if request.GET.get('search'):
        form = SearchForm(request.GET)
        if form.is_valid():
            query_string = form.cleaned_data['search']
            entry_query = get_query(query_string, ['title'])
            recipes = collection.recipes.filter(entry_query, tags=tag,).order_by('title')
            return render(request, 'recipes/view_collection.html', {
                'collection': collection,
                'form': form,
                'query': query_string,
                'recipes': recipes
            })
        else:
            messages.error(request, 'Could not filter. Please try again.')

    return render(request, 'recipes/view_collection.html', {
        'collection': collection,
        'recipes': recipes,
        'form': form
    })


@login_required
def edit_collection(request, collection_id=None):
    collection = RecipeCollection()
    if collection_id:
        collection = get_object_or_404(RecipeCollection, pk=collection_id, users=request.user)
    form = CollectionForm(instance=collection)
    if request.method == 'POST':
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
    if request.method == 'POST':
        if request.POST.get('delete') == 'yes':
            collection.delete()
            messages.success(request, 'Deleted collection')
        else:
            messages.error(request, 'Could not delete collection. Please try again. ')
    return redirect('recipes:index')


@login_required
def view_collection(request, collection_id):
    query_string = ''
    collection = get_object_or_404(RecipeCollection, pk=collection_id, users=request.user)
    recipes = collection.recipes.all().order_by('title')
    form = SearchForm()
    if request.GET.get('search'):
        form = SearchForm(request.GET)
        if form.is_valid():
            query_string = form.cleaned_data['search']
            entry_query = get_query(query_string, ['title'])
            recipes = collection.recipes.filter(entry_query).order_by('title')
            return render(request, 'recipes/view_collection.html', {
                'collection': collection,
                'form': form,
                'query': query_string,
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
    if request.method == 'POST':
        if request.POST.get('delete') == 'yes':
            collection.recipes.remove(recipe)
            messages.success(
                request,
                'Removed recipe {} from collection {}'.format(recipe.title, collection.title))
        else:
            messages.error(request, 'Could not delete recipe. Please try again. ')
    return redirect('recipes:view_collection', collection_id=collection.pk)


@login_required
def edit_recipe_in_collection(request, collection_id, recipe_id=None):
    collection = get_object_or_404(RecipeCollection, pk=collection_id, users=request.user)
    recipe = Recipe()
    if recipe_id:
        recipe = get_object_or_404(Recipe, pk=recipe_id)
    form = RecipeForm(instance=recipe)
    if request.method == 'POST':
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
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(username=form.cleaned_data['username'])
                collection.users.add(user)
                messages.success(
                    request,
                    'Added {} to collection {}'.format(user.username, collection.title))
                return redirect('recipes:view_collection', collection_id=collection.pk)
            except ObjectDoesNotExist:
                messages.error(request, 'User does not exist')
    return render(request, 'recipes/add_user_to_collection.html', {
        'form': form, 'collection': collection})
