from email import message
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'username created {username}!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, "users/signup.html", context={'form':form})



def signin(request):
    #form = UserLoginForm()

    return render(request, "users/signin.html", )