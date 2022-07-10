from http import client
from django.shortcuts import render
from mains.models import Clients, Projects
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProjectSerializer, ClientSerializer, ClientListSerializer
from rest_framework import status
from django.shortcuts import render



#Clients api endpoints

@api_view(['GET', 'POST'])
def getClients(request):
    if request.method == "GET":
        client_all = Clients.objects.all()
        client_ser = ClientListSerializer(client_all, many= True)
        return Response(client_ser.data)
    
    elif request.method == "POST":
        client_ser = ClientListSerializer(data=request.data)
        
        if client_ser.is_valid():
            client_ser.save(created_by=request.user)        
        return Response(client_ser.data)



@api_view(['GET','PUT', 'DELETE'])
def getClientdet(request, pk):
    if request.method == "GET":
        client = Clients.objects.get(id=pk)
        client_ser = ClientSerializer(client)
        return Response(client_ser.data)

    elif request.method == "PUT":
        client_update = Clients.objects.get(id=pk)
        client_ser = ClientListSerializer(instance= client_update, data=request.data)
        if client_ser.is_valid():
            client_ser.save()        
        return Response(client_ser.data)

    elif request.method == "DELETE":
        client_update = Clients.objects.get(id=pk)
        client_update.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)




#projects api endpoints

@api_view(['GET', 'POST'])
def getProjects(request, pk):
    if request.method == "GET":
        project_all = Projects.objects.filter(client=pk)
        project_ser = ProjectSerializer(project_all, many= True)
        return Response(project_ser.data)

    elif request.method == "POST":
        project_ser = ProjectSerializer(data=request.data)
        project_ser.client = Clients.objects.get(id=pk)
        if project_ser.is_valid():
            project_ser.save(client=Clients.objects.get(id=pk))        
        return Response(project_ser.data)      

@api_view(['GET','PUT', 'DELETE'])
def getProjectdet(request, pk):
    if request.method == "GET":
        project_all = Projects.objects.get(pk=pk)
        project_ser = ProjectSerializer(project_all)
        return Response(project_ser.data)

