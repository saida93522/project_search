from django.shortcuts import render, redirect
from django.contrib import messages

from .models import User,Profile

def profiles(request):
    users = Profile.objects.all()
    context = {'users':users}
    return render(request, 'users/profiles.html',context)