""" Contains helper functions for users app."""

from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Profile, Skills


def paginate_profiles(request, users,results):
    """ Paginate users."""

    page = request.GET.get('page') #first page of result
    # results = 3 #3 result per-page
    paginator = Paginator(users, results)

    try:
        #if requested page is an integer
        #render a Page object for the given 1-based page number.
        users = paginator.page(page)
    except PageNotAnInteger as e:
        #if page is not past in(page=1) or not an integer return the first page
        page = 1
        users = paginator.page(page)
        print(e)
    except EmptyPage as empty_page:
        #if page contains no results,if a user goes out of that index
        page = paginator.num_pages
        users = paginator.page(page)
        print(empty_page)

    # minimiza num of page btn. if you have a thousand pages, you will only see
    # first 4 buttons from the left and last button on right.
    
    # the current page minus four
    left_index = (int(page) - 4)
    if left_index < 1:
        left_index = 1

        
    right_index = (int(page) + 5)
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1
        
    custom_range = range(left_index, right_index)

    return custom_range, users






def search_profiles(request):
    """ Search for developers/profiles."""
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
    