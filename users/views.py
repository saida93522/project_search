from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import User, Profile, Skills


# Authentication

def register_user(request):
    context = {}
    return render(request, 'signup.html',context)
   

def login_user(request):
    """Authenticate username and password. verfiy credentials are met.
    if the user exists in sessions db redirect to homepage.

    Args:
        request ([POST]): username and password data to login.

    Returns:
        [message or homepage]: if user exists, user will be redirected to the homepage. otherwise an error message will be displayed.
    """
    
    if request.method == 'POST':
        # extract username password from POST dict
        username = request.POST['username'].lower()
        password = request.POST['password']
        
        # verify user exists in sessions db
        try:
            user = User.objects.get(username=username)
        except Exception:
            print('username OR password does not exist.')
            messages.error(request,'username OR password does not exist.')
            
        # if user does exist, verify credentials are met
        #return User object that matches these credentials
        user = authenticate(request, username=username,password=password)
        if user is not None:
            # creates a session for this user in the db
            # then adds that session into the browser cookies.i.e cookies=sessionid
            login(request, user)
            return redirect('profiles')
        else:
            print('username OR password is incorrect.')
            messages.error(request,'username OR password is incorrect.')
        
    context = {}
    return render(request, 'users/login_register.html')

def logout_user(request):
    pass








# Profile
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

def skills(request,pk):
    pass
    # skills = Skills.objects.get(id=pk)
    # context = {'skills':skills}
    # return render(request, 'profile.html',context)


