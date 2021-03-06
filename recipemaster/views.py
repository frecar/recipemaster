# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import redirect, render

from recipemaster.recipes.forms import SignUpForm


def registration(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User successfully created. Now you can login.')
            return redirect('recipes:index')
        else:
            messages.error(request, 'Could not create user. Please try again.')
    return render(request, 'registration/registration.html', {'form': form})


def password_reset(request):
    form = PasswordResetForm()
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            messages.success(request, 'A link to reset the password is sent to your email.')
        else:
            messages.error(request, 'Could not send email. Please try again.')
    return render(request, 'registration/password_reset.html', {'form': form})
