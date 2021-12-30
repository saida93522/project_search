from django.shortcuts import render, redirect
from django.contrib import messages

from .models import User,Profile

def profiles(request):
    context = {}
    return render(request, 'users/profiles.html',context)