from dataclasses import field
from http import client
from rest_framework import serializers
from mains.models import Projects, Clients

class ProjectSerializer(serializers.ModelSerializer):
    assign_to = serializers.StringRelatedField(many=True) 
    client = serializers.StringRelatedField()
    class Meta:
        model = Projects
        fields = '__all__'


class ClientListSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField() 

    class Meta:
        model = Clients  
        fields = ('id', "client_name", "created_at", "created_by")      
        #fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField() 
    projects = serializers.StringRelatedField(many=True)    
    class Meta:
        model = Clients  
        fields = ('id', "client_name", "created_at", "created_by", "projects")      
        #fields = '__all__'