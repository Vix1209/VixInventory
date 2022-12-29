from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import forms
from .models import Profile

# Create your views here.
def register (request):
    if request.method == 'POST':
        form =  forms.CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-profile_edit')
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



def profile_edit (request):
    if request.method == 'POST':
        form =  forms.UserProfileForm(request.POST)
    
        if form.is_valid():
            form.save()
            return redirect('user-login')
    else:
        form =  forms.UserProfileForm()
        
    context = {
        'form': form,
    }
    return render(request, 'user/profile_edit.html', context)


def profile (request):
    return render(request, 'user/profile.html')  