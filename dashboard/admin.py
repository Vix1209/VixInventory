from django.contrib import admin
from . import models
from django.contrib.auth.models import Group  

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')
    list_filter  = ('category',)


admin.site.register(models.Product, ProjectAdmin)
admin.site.register(models.Order)
# admin.site.unregister(Group) 
admin.site.site_header = 'VixInventory Admin' # to change the header name in the admin panel

