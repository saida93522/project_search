from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def projects(request):
    return render(request,'projects/projects.html')

def single_project(request):
    return render(request,'projects/single_project.html')