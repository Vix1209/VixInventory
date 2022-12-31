from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register', views.register, name= 'user-register'),
    path('', auth_views.LoginView.as_view(template_name = 'user/login.html') , name= 'user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'user/logout.html'), name= 'user-logout'),
    path('profile/', views.profile, name = 'user-profile'),
    path('profile/edit/', views.profile_update, name = 'user-profile-update'),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
