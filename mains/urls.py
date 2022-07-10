
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registerclient/', views.registerclient, name='registerclient'),
    path('createproject/', views.createproject, name='createproject'),
    path('myprojects/', views.myprojects, name='myprojects'),
    ] 
    
# 