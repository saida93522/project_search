from django.shortcuts import render
from  .models import Project, Review, Tag
# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def projects(request):
    projects = Project.objects.all()
    

    
    context = {'projects':projects}
    return render(request,'projects/projects.html', context)

def single_project(request,pk):
    projectObj = Project.objects.get(id=pk)
  
    context = {'project':projectObj}
    return render(request,'projects/single_project.html',context)