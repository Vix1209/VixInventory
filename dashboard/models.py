from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# CATEGORY is the choicelist which will be displayed in the frontend
CATEGORY = (
    
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
    
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices = CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)
    
    #null = True is used only during development and not production
    
    
    #To rename the models in the admin to your heart desire
    class Meta:
        verbose_name_plural = 'Product'
    
    def __str__(self):
        return f'{self.name}'
    
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null = True) # This creates a relationship between the order model and the Product model using a Foreign Key
                                                                                # 'on_delete = models.CASCADE' this means if an item in the product model is deleted, the same thing will happen in the order model
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True) #the model 'User' is the same defined in the admin panel already created for us
    order_quantity = models.PositiveIntegerField(null = True) # this means that the number of orders will always be positive
    date = models.DateTimeField(auto_now_add=True)
    
    
    #To rename the models in the admin to your heart desire
    class Meta:
        verbose_name_plural = 'Order'
        
    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'
    
    
    
