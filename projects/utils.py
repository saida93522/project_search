""" Contains helper functions for projects app."""

from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Project, Tag

def paginate_projects(request, projects,results):
    """ Paginate projects."""

    page = request.GET.get('page') #first page of result
    # results = 3 #3 result per-page
    paginator = Paginator(projects, results)

    try:
        #if requested page is an integer
        #render a Page object for the given 1-based page number.
        projects = paginator.page(page)
    except PageNotAnInteger as e:
        #if page is not past in(page=1) or not an integer return the first page
        page = 1
        projects = paginator.page(page)
        print(e)
    except EmptyPage as empty_page:
        #if page contains no results,if a user goes out of that index
        page = paginator.num_pages
        projects = paginator.page(page)
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

    return custom_range, projects

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