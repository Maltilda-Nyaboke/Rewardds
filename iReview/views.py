from hashlib import new
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import RegisterForm,UpdateProfileForm,AddProjectForm,RatingForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer

# Create your views here.

def home(request):
    projects = Project.objects.all()
    new_project = Project.objects.last()

    if request.method=='POST':
        user=request.user
        form=AddProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.user=user
            project.save()
            return redirect('home')
    else:
            form=AddProjectForm()
    return render(request,'index.html',{'form':form,'projects':projects,'new_project':new_project})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index.html')
    else:        
        form = RegisterForm()
    return render(request,'register.html',{'form':form})  


def login_user(request):
    form = AuthenticationForm()
    context = {'form':form}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request,'registration/login.html',context)  
    else:
        return render(request,'registration/login.html',context)        
@login_required
def logout_user(request):
    logout(request)
    return redirect('login')   

@login_required
def profile(request):
    user = request.user.pk
    # profile = Profile.objects.all()
    profile = Profile.objects.filter(user=request.user.pk)
    projects = Project.objects.filter(user=request.user.pk)
    context = {'profile': profile,'projects': projects}
    return render(request,'profile.html',context)   
@login_required
def update_profile(request):
    form = UpdateProfileForm()
    user = request.user
    profile = Profile.objects.get(user=user)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile.profile_photo = form.cleaned_data.get('profile_photo')
            profile.bio = form.cleaned_data.get('bio')
            profile.save()
            return redirect('profile')
        else:
            form = UpdateProfileForm()    
    return render(request,'update_profile.html',{'form':form})    
@login_required
def search_results(request):
    query = request.GET.get('query')
    if query:
        projects = Project.objects.filter(
            Q(title__icontains=query)
        )
        context = {'projects': projects}
        return render(request,'search.html',context)
@login_required
def project(request,id):
    form = RatingForm()
    project = Project.objects.filter(id=id).first()
    ratings = Rating.objects.filter(user=request.user,id=id).first()
    rating_status = None
    if rating_status is None:
        rating_status = False
    else:
        rating_status = True    
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.project = project
            rate.save()
            project_ratings = Rating.objects.filter(project=project)
            design_ratings = [d.design for d in project_ratings]
            design_average = sum(design_ratings) / len(design_ratings)
            usability_ratings = [us.usability for us in project_ratings] 
            usability_average = sum(usability_ratings) / len(usability_ratings)
            content_ratings = [content.content for content in project_ratings]
            content_average = sum(content_ratings) / len(content_ratings)
            score = (design_average + usability_average + content_average) / 3
            print(score)
            rate.design_average = round(design_average, 2)
            rate.usability_average = round(usability_average, 2)
            rate.content_average = round(content_average, 2)
            rate.score = round(score, 2)
            rate.save()
            return HttpResponseRedirect(request.path_info)   
    context = {'project':project, 'ratings':ratings,'form':form,'rating_status':rating_status}    
    return render(request, 'project.html',context)
@login_required
def new_project(request):
    if request.method=='POST':
        user=request.user
        form=AddProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.user=user
            project.save()
            return redirect('home')
    else:
            form=AddProjectForm()
    return render(request,'new_project.html',{'form':form}) 

class ProfileList(APIView):
    def get(self, request, format = None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles,many=True)
        return Response(serializers.data)              

class ProjectList(APIView):
    def get(self, request, format = None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects,many=True)
        return Response(serializers.data)              
