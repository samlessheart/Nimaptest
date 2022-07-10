from django.db import models
from django.contrib.auth.models import User

 

class Clients(models.Model):
    client_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, default=1)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.client_name 

class Projects(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
 #   created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    assign_to  = models.ManyToManyField(User, related_name="projects",  blank=True)
    client = models.ForeignKey(Clients, on_delete=models.SET_NULL, null=True, blank=True, related_name='projects')
    
    def __str__(self):
        return self.name 

