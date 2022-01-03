""" Contains helper functions for projects app."""

from django.db.models import Q
from django.core.paginator import Paginator

from .models import Project, Tag

def search_projects(request):
    """ Search for projects."""
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags_query = Tag.objects.filter(name__icontains=search_query)
    
    projects = Project.objects.distinct().filter(
        Q(title__icontains = search_query)|
        Q(description__icontains = search_query)|
        Q(owner__name__icontains = search_query)|
        Q(tags__in = tags_query)
        
        )
    return projects, search_query