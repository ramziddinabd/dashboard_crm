from django.shortcuts import render, redirect
from . forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def mainPage(request):
    return render(request, "loginapp/mainpage.html")


def register_user(request):
    form = CreateUserForm
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('login')

    context = {'form':form}
    return render(request, 'loginapp/index.html', context)



def login_user(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                messages.info(request, "ERORR")
            
        context = {}

        return render(request, 'loginapp/index.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')
