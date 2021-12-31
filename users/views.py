from django.shortcuts import render, redirect
from django.contrib import messages

from .models import User, Profile, Skills

def profiles(request):
    users = Profile.objects.all()
    context = {'users':users}
    return render(request, 'users/profiles.html',context)


def profile(request,pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile':profile}
    return render(request, 'profile.html',context)