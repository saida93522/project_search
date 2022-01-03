""" Contains helper functions."""

from django.db.models import Q
from .models import Profile, Skills
def search_profiles(request):
    """ A search function to trigger for all searches on the webpage."""
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    print('SEARCH: ', search_query)
    
    # renders only one profile instance related to that skill. avoids duplicates
    skills = Skills.objects.filter(skill_name__icontains=search_query)

    users = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(short_intro__icontains=search_query) |
        Q(username__icontains=search_query) |
        Q(skills__in=skills)
        )
    return users, search_query
    