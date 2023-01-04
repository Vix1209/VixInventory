from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.index, name ='dashboard-index'),
    path('staff/', views.staff, name = 'dashboard-staff'),
    path('staff/detail/<int:pk>', views.staff_detail, name = 'dashboard-staff-detail'),
    path('product/', views.products, name = 'dashboard-products'),
    path('product/delete/<int:pk>/', views.product_delete, name = 'dashboard-product-delete'),
    path('product/edit/<int:pk>/', views.product_update, name = 'dashboard-product-update'),
    path('order/', views.orders, name = 'dashboard-orders'),
]


# <int:pk> this means the primary key(pk) being passed will be an integer