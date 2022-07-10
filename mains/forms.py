from django import forms
from django.forms import (fields, widgets, Textarea, NumberInput, Select, DateField,  SelectMultiple, CheckboxSelectMultiple)
from .models import Clients, Projects


class clientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['client_name']
        widgets = {
            'client_name': Textarea(attrs={'rows': 1,'class': 'form-control col-6'}),
        }


class projectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['name', 'assign_to', 'client' ]
        widgets = {
            'name': Textarea(attrs={'rows': 1,'class': 'form-control col-6'}),
            'assign_to': CheckboxSelectMultiple(attrs={'rows': 1,'class': 'form-control col-6'}),
            'client': Select(attrs={'rows': 1,'class': 'form-control col-6'}),
        }
