from django.shortcuts import render, redirect
from  .models import Project, Review, Tag
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.shortcuts import render

from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    
    context = {'projects':projects}
    return render(request,'projects/projects.html', context)

def single_project(request,pk):
    projectObj = Project.objects.get(id=pk)
  
    context = {'project':projectObj}
    return render(request,'projects/single_project.html',context)

@login_required(login_url='login')
def create_project(request):
    form = ProjectForm() #extensiate from projectForm
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    
    context = {'form':form}
    return render(request,'projects/project_form.html', context )

@login_required(login_url='login')
def edit_project(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project) 
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    
    context = {'form':form}
    return render(request,'projects/project_form.html', context )

@login_required(login_url='login')
def delete_project(request,pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object':project}
    return render(request,'projects/delete_template.html', context )