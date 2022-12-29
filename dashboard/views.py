from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

# either put the login_url here, or in settings.py

# @login_required(login_url='user-login')
# def index(request):
#    return render(request, 'dashboard/index.html')

# @login_required(login_url='user-login')
# def staff(request):
#     return render(request, 'dashboard/staff.html')

# @login_required(login_url='user-login')
# def products(request):
#     return render(request, 'dashboard/products.html')    

# @login_required(login_url='user-login')
# def orders(request):
#     return render(request, 'dashboard/orders.html')

# @login_required(login_url='user-login')
# def profile(request):
#     return render(request, 'dashboard/admin.html')




@login_required
def index(request):
   return render(request, 'dashboard/index.html')

@login_required
def staff(request):
    return render(request, 'dashboard/staff.html')

@login_required
def products(request):
    return render(request, 'dashboard/products.html')    

@login_required
def orders(request):
    return render(request, 'dashboard/orders.html')

