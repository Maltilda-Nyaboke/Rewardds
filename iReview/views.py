from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from .models import *

# Create your views here.

def home(request):
    project = Project.objects.all()
    return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index.html')
    else:        
        form = RegisterForm()
    return render(request,'register.html',{'form':form})  


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request,'index.html')
        else:
            return render(request,'/registration/login.html')  
    else:
        return render(request,'/registration/login.html')        

def logout_user(request):
    logout(request)
    return redirect('login')   


def profile(request):
    return render(request,'profile.html')   

def update_profile(request):
    return render(request,'update_profile.html')    


def new_project(request):
    return render(request,'new_project.html')           

