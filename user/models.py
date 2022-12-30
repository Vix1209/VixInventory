from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile (models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True) #this denotes that one user is equal to one profile
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    image =  models.ImageField(default = 'avatar.png', upload_to= 'Profile_Images', blank= True, null=True)
    
    def __str__(self):
        return f"{self.staff}'s Profile"

 
