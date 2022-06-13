from django.shortcuts import render,redirect
from .forms import RegisterForm,UpdateProfileForm
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
    form = UpdateProfileForm()
    if request.method == 'POST':
        user = request.user.id
        form = UpdateProfileForm(request.POST,request.FILES)
        profile = Profile.objects.get(user_id=user)
        if form.is_valid():
            profile.profile_photo = form.cleaned_data.get('profile_photo')
            profile.bio = form.cleaned_data.get('bio')
            profile.save()
            return redirect('profile')
        else:
            form = UpdateProfileForm()    
    return render(request,'update_profile.html',{'form':form})    

def search_results(request):
  form=AddProjectForm()
  if 'search' in request.GET and request.GET['search']:
    
    title_search = request.GET.get('search')
    print(title_search)
    searched_projects = Project.search_by_title(title_search)
  
    message = f"{title_search}"
    return render(request, 'search.html', {"message":message, "projects":searched_projects,"form":form})
  else:
    message = "You have not yet made a search"

    return render(request, 'search.html', {"message":message})


def new_project(request):
    return render(request,'new_project.html')           

