# -*- coding: utf-8 -*-
from django.shortcuts import redirect, render
from recipemaster.recipes.forms import SignUpForm
from django.contrib import messages


def registration(request):
    form = SignUpForm()
    if request.POST:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created. Please login.')
            return redirect('recipes:index')
        else:
            messages.error(request, 'Could not create user. Please try again.')
    return render(request, 'registration/registration.html', {'form': form})
