from django.shortcuts import render, redirect
from  .models import Project, Review, Tag
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from django.db.models import Q
from .utils import search_projects

from .forms import ProjectForm


def projects(request):
    projects, search_query = search_projects(request)
    
    context = {'projects':projects, 'search_query':search_query}
    return render(request,'projects/projects.html', context)

def single_project(request,pk):
    projectObj = Project.objects.get(id=pk)
  
    context = {'project':projectObj}
    return render(request,'projects/single_project.html',context)

@login_required(login_url='login')
def create_project(request):
    profile = request.user.profile
    form = ProjectForm() #extensiate from projectForm
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile #set the currently logged in user to this project
            messages.success(request,('Project was added successfully!'))
            project.save()
            return redirect('account')
    
    context = {'form':form}
    return render(request,'projects/project_form.html', context )

@login_required(login_url='login')
def edit_project(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project) 
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request,('Project was updated successfully!'))
            return redirect('account')
    
    context = {'form':form}
    return render(request,'projects/project_form.html', context )

@login_required(login_url='login')
def delete_project(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        messages.error(request,('Project was deleted successfully!'))
        return redirect('account')
    context = {'object':project}
    return render(request,'delete_template.html', context )