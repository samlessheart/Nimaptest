from django.shortcuts import redirect, render

from mains.models import Clients, Projects
from .forms import clientForm, projectForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'mains/home.html')



@login_required(login_url='/user/signin/')
def registerclient(request):
    form = clientForm()
    context = {"form":form}
    if request.method == 'POST':
        form = clientForm(request.POST) 
        if form.is_valid():
            client_name = form.cleaned_data['client_name']
            created_by = request.user 
            client = Clients.objects.create(client_name, created_by)
            client.save()
            messages.success(request, f'{client} is created')
            return redirect('home')

    return render(request, 'mains/registerclient.html', context)


@login_required(login_url='/user/signin/')
def createproject(request):
    form = projectForm()
    context = {"form":form}
    if request.method == 'POST':
        form = projectForm(request.POST) 
        if form.is_valid():
            name = form.cleaned_data['name']
            assign_to = form.cleaned_data['assign_to']
            client = form.cleaned_data['client']
            proj_obj = Projects.objects.create(name=name, assign_to=assign_to, client=client)
            proj_obj.save()
            messages.success(request, f'{proj_obj} is created')
            return redirect('home')

    return render(request, 'mains/createproject.html', context)



@login_required(login_url='/user/signin/')
def myprojects(request):
    project_list = Projects.objects.filter(assign_to=request.user)
    context = {'proj_obj':project_list}
    return render(request, 'mains/myprojects.html', context)