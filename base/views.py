from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



@login_required(login_url='/login/')
def index(request):
    return render(request, 'base/index.html')

def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    return render(request, 'accounts/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('login_user')

def register_user(request):
    return render(request, 'accounts/register.html', {})