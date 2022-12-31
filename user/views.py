from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . import forms
from .models import Profile

# Create your views here.
def register (request):
    if request.method == 'POST':
        form =  forms.CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')
    else:
        form =  forms.CreateUserForm()
        
    context = {
        'form': form,
    }
    return render(request, 'user/register.html', context)


def login (request):
    return render(request, 'user/login.html')


def logout (request):
    return render(request, 'user/logout.html')


def profile (request):
    return render(request, 'user/profile.html')  


def profile_update(request):
    if request.method == 'POST':
        user_form = forms.UserUpdateForm(request.POST, instance = request.user)
        profile_form = forms.ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect ('user-profile')
        
    else:
        user_form = forms.UserUpdateForm(instance = request.user)
        profile_form  = forms.ProfileUpdateForm(instance = request.user.profile)
        
    context = {
        'user_form' : user_form,
        'profile_form' : profile_form,
    }
    return render(request, 'user/profile_update.html', context)
    