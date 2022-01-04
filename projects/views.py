from django.shortcuts import render, redirect
from  .models import Project, Review, Tag
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .utils import search_projects, paginate_projects

from .forms import ProjectForm, ReviewForm


def projects(request):
    projects, search_query = search_projects(request)
    custom_range, projects = paginate_projects(request, projects,6)
    
    
    context = {'projects':projects, 'search_query':search_query,'custom_range':custom_range}
    return render(request,'projects/projects.html', context)

def single_project(request,pk):
    projectObj = Project.objects.get(id=pk)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()
        # update project votecount
        projectObj.get_vote_count
        
        messages.success(request, 'Your review was successfully posted.')
        return redirect('project', pk=projectObj.id) #send user back to their page

      
        
    context = {'project':projectObj, 'form':form}
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