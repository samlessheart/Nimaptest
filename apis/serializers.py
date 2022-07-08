from dataclasses import field
from rest_framework import serializers
from mains.models import Projects, Clients

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    #created_by = serializers.CharField(source="User.username", read_only=True)

    class Meta:
        model = Clients  
        fields = ('id', "name", "created_at", "created_by", 'projects_set')      
        #fields = '__all__'