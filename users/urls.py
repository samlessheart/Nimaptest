
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='users/signin.html'), name='signin'),
    path('signout/', auth_views.LogoutView.as_view(template_name='users/signout.html'), name='signout'),
    
    ]
