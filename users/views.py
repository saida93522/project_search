from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError
from django.http import HttpResponseForbidden 
from django.contrib import messages

from django.db.models import Q
from .models import Profile, Message
from .forms import UserRegisterForm, ProfileForm, SkillForm


# Authentication

def register_user(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) #hold before processing
            user.username = user.username.lower()
            user.save()
            
            messages.success(request,f'Welcome {user.name}.')
            # log user in and redict them to profile page
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request,f'An error occurred during registration.')
            return render(request, '404.html')
    context = {'form':form}
    return render(request, 'users/signup.html',context)
   

def login_user(request):
    """Authenticate username and password. verfiy credentials are met.
    if the user exists in sessions db redirect to homepage.

    Args:
        request ([POST]): username and password data to login.

    Returns:
        [message or homepage]: if user exists, user will be redirected to the homepage. otherwise an error message will be displayed.
    """
    
    # restrict logged in user from seeing the log in page
    if request.user.is_authenticated:
        return redirect('profiles')
    
    if request.method == 'POST':
        # extract username password from POST dict
        username = request.POST['username'].lower()
        password = request.POST['password']
        
        # verify user exists in sessions db
        try:
            user = User.objects.get(username=username)
            # messages.info(request, f'{username} Successfully Logged In') 
        except:
            messages.error(request,'Oh no!, Failed to login.')
            
            
        # if user does exist, verify credentials are met
        #return User object that matches these credentials
        user = authenticate(request, username=username,password=password)
        if user is not None:
            # creates a session for this user in the db
            # then adds that session into the browser cookies.i.e cookies=sessionid
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request,'username OR password is incorrect.')
        
  
    return render(request, 'users/login_register.html')

def logout_user(request):
    """ Removes the authenticated user's ID from the request and deletes their session data.

    Args:
        request ([GET]): [gets current logged user id and flush session]

    Returns:
        [redirect login page]: [redirects user to the login page]
    """
    # deletes token created by session db
    username = request.user.username
    logout(request)
    print(username)
    messages.success(request,f'Successfully logged out. We will miss you.')
    return redirect('login')

#  Profile
def profiles(request):
    users = Profile.objects.all()
    context = {'users':users}
    return render(request, 'users/profiles.html',context)

def profile(request,pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skills_set.exclude(skill_description__exact="")
    otherSkills = profile.skills_set.filter(skill_description="")
    context = {'profile':profile, 'topSkills':topSkills,'otherSkills':otherSkills }
    return render(request, 'users/user_profile.html',context)

@login_required(login_url='login')
def user_account(request):
    """ Responds with the logged-in user's profile. """
    profile = request.user.profile

    skills = profile.skills_set.all()
    projects = profile.project_set.all()
   

    context = {'profile':profile, 'skills':skills,'projects':projects}
    return render(request, 'users/account.html',context)

@login_required(login_url='login')
def edit_account(request):
    profile = request.user.profile # returns the logged in user profile
    form = ProfileForm(instance=profile)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,('Your profile was successfully updated!'))
            return redirect('account')
        
    context = {'form':form}
    return render(request, 'users/profile_form.html',context)

@login_required(login_url='login')
def create_skill(request):
    profile = request.user.profile
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request,('Skill was added successfully!'))
            return redirect('account')
    context = {'form':form}
    return render(request, 'users/skill_form.html',context)

@login_required(login_url='login')
def edit_skill(request,pk):
    profile = request.user.profile
    skill = profile.skills_set.get(id=pk)
    form = SkillForm(instance=skill)

    
    if request.method == 'POST':
        form = SkillForm(request.POST,instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request,('Skill was updated successfully!'))
            return redirect('account')
        
    context = {'form':form}
    return render(request, 'users/skill_form.html',context)

@login_required(login_url='login')
def delete_skill(request,pk):
    profile = request.user.profile
    skill = profile.skills_set.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        messages.error(request,('Skill was deleted successfully!'))
        return redirect('account')
    context = {'object':skill}
    return render(request, 'delete_template.html', context)


