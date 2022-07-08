from django.shortcuts import render
from mains.models import Clients, Projects
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProjectSerializer, ClientSerializer, ClientListSerializer
from rest_framework import status


@api_view(['GET'])
def getClients(request):
    client_all = Clients.objects.all()
    client_ser = ClientListSerializer(client_all, many= True)
    return Response(client_ser.data)

@api_view(['GET'])
def getClientdet(request, pk):
    client_all = Clients.objects.get(id=pk)
    client_ser = ClientSerializer(client_all)
    return Response(client_ser.data)

@api_view(['POST'])
def createClient(request, ):    
    client_ser = ClientListSerializer(data=request.data)
    if client_ser.is_valid():
        
        client_ser.save()        
    return Response(client_ser.data)


@api_view(['POST'])
def updateClient(request, pk):
    client_update = Clients.objects.get(id=pk)
    client_ser = ClientSerializer(instance= client_update, data=request.data)
    if client_ser.is_valid():
        client_ser.save()        
    return Response(client_ser.data)


@api_view(['DELETE'])
def deleteClient(request, pk):
    client_update = Clients.objects.get(id=pk)
    client_update.delete()
    return Response(status = 204)


@api_view(['GET'])
def getProjects(request):
    project_all = Projects.objects.all()
    project_ser = ProjectSerializer(project_all, many= True)
    return Response(project_ser.data)

@api_view(['GET'])
def getProjectdet(request, pk):
    project_all = Projects.objects.get(pk=pk)
    project_ser = ProjectSerializer(project_all)
    return Response(project_ser.data)

