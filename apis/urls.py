
from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('clients/', views.getClients, name='getClients'),
    path('clients/<int:pk>/', views.getClientdet, name='getClientdet'),
    path('clients/<int:pk>/projects', views.getProjects, name='getProjects'),
    
 ]
