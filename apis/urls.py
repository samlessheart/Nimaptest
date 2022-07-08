
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.getClients, name='getClients'),
    path('clients/<int:pk>/', views.getClientdet, name='getClientdet'),
    path('createClient/', views.createClient, name='createClient'),
    path('deleteClient/<int:pk>/', views.deleteClient, name='deleteClient'),
    path('updateClient/<int:pk>/', views.updateClient, name='updateClient'),
    path('projects/', views.getProjects, name='getProjects'),
    path('projects/<int:pk>/', views.getProjectdet, name='getProjectdet'),
 ]
