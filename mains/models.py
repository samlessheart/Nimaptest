from django.db import models
from django.contrib.auth.models import User

 

class Clients(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True )
    

    def __str__(self):
        return self.name 

class Projects(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
 #   created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    assign_to  = models.ManyToManyField(User, related_name="assign_to",  blank=True)
    client = models.ForeignKey(Clients, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name 

