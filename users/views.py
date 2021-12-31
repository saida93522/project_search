from django.shortcuts import render, redirect
from django.contrib import messages

from .models import User, Profile, Skills

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
