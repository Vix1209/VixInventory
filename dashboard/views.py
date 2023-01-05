from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages 

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
    workers = User.objects.all()
    workers_count = workers.count()
    
    items = Product.objects.all()   
    items_count = items.count()
    
    order = Order.objects.all()
    order_count = order.count()
    
    
    orders = Order.objects.all()
    products = Product.objects.all()
    if request.method == 'POST':
        forms = OrderForm(request.POST)
        if forms.is_valid():
            instance =  forms.save(commit=False) #this line of code "commit = False" does a very crucuial task of pausing the save() method process from occuring
            instance.staff = request.user # That is to allow this line of code w=to run successfully. This line assigns the currently authenticated user 'request.user' to the particular order it was created from
            instance.save() # then and only then can this the form (instance) be saved
            return redirect('dashboard-index')
    else:
        forms = OrderForm()
    context = { 
        'orders':orders,
        'forms': forms,
        'products': products,
        'items_count':items_count,
        'workers_count':workers_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/index.html', context)




@login_required
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    
    items = Product.objects.all()   
    items_count = items.count()
    
    order = Order.objects.all()
    order_count = order.count()
    
    context = {
        'workers':workers,
        'items_count':items_count,
        'workers_count':workers_count,
        'order_count': order_count,

    }
    
    return render(request, 'dashboard/staff.html', context)


@login_required
def staff_detail(request, pk):
    workers = User.objects.get(id = pk)
    
    context = {
        'workers': workers,
    }
    return render(request, 'dashboard/staff_detail.html', context)




@login_required
def products(request):
    workers = User.objects.all()
    workers_count = workers.count()
    
    order = Order.objects.all()
    order_count = order.count()
    
    #CRUD:

    #READ
    # This listens for an entry in the form in the Products page, grabs the input, vaidates if its true and saves to the database.
    if request.method =='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            message = messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-products')
    else:
        form = ProductForm()
        
        
    #CREATE
    # this grabs all the data in the product table in the database, and saves into the variable 'items'
    items = Product.objects.all()   #this collects all the data from the product model
    #items = Product.objects.raw('SELECT * FROM dashboard_product')   #Normal SQL logic
    items_count = items.count()
    
    # in the context, the dictionary shows the 'items' key which is what will be written in the frontend. #
    # while the value represents the items variable above
    # by doing that, you cause the frontend to read directly from the backend into the database.
    context = {
        'items': items,
        'form': form,
        'items_count':items_count,
        'workers_count':workers_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/products.html', context)    


#UPDATE
@login_required
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
    else:
        form = ProductForm(instance=item)

    context  = {
        'form': form
    }
    return render(request, 'dashboard/product_update.html', context)


#DELETE
@login_required
def product_delete(request, pk): #pk is the argument that represents the primary key for each item in the table
    
    #this grabs the ID of the objects in the Products model and saves in the variable 'items'
    item = Product.objects.get(id = pk)
    
    # a form is provided with a button inside with input type submit. on submitting it (POST), a logic is invoked
    if request.method == 'POST':
        
        # this deletes the information from the database
        item.delete()
        
        #then redirects to the products page
        return redirect('dashboard-products')
    return render(request, 'dashboard/product_delete.html')
    
    
  
    
@login_required
def orders(request):
    workers = User.objects.all()
    workers_count = workers.count()
    
    items = Product.objects.all()   
    items_count = items.count()
    
    order = Order.objects.all()
    order_count = order.count()
           
    context = {
        'order': order,
        'items_count':items_count,
        'workers_count':workers_count,
        'order_count': order_count,

    }
    return render(request, 'dashboard/orders.html', context )


