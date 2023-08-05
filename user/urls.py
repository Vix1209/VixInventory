from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #will have logic being put in views.py
    path('register', views.register, name= 'user-register'),
    path('profile/', views.profile, name = 'user-profile'),
    path('profile/edit/', views.profile_update, name = 'user-profile-update'),
    
    # these have django authviews to handle them
    path('', auth_views.LoginView.as_view(template_name = 'user/login.html') , name= 'user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'user/logout.html'), name= 'user-logout'),
    
    # input these path routes for our forgot password setup after which we provide the email and password details to enable django log in successfully
    path('password/reset/', auth_views.PasswordResetView.as_view(template_name = 'user/password_reset.html'), name = 'password_reset'),
    path('password/reset/success/', auth_views.PasswordResetDoneView.as_view(template_name = 'user/password_reset_done.html'), name = 'password_reset_done'),
    path('password/reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'user/password_reset_confirm.html'), name = 'password_reset_confirm'),
    path('password/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name = 'user/password_reset_complete.html'), name = 'password_reset_complete'),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
