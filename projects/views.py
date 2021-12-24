from django.shortcuts import render
from  .models import Project, Review, Tag
# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def projects(request):
    projects_List = Project.objects.all()
   
    projects_tag = Project.objects.first()
    projects_tag.tags.all()
    context = {'projects':projects_List, 'tags':projects_tag}
    return render(request,'projects/projects.html', context)

def single_project(request,pk):
    projects_List = Project.objects.get(id=pk)
  
    context = {'project':projects_List}
    return render(request,'projects/single_project.html',context)