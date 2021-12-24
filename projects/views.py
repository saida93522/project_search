from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]

def home(request):
    return render(request,'home.html')

def projects(request):
    msg = 'projects'
    number = 10
    context = {'msg':msg, 'num':number, 'projects':projectsList}
    return render(request,'projects/projects.html', context)

def single_project(request,pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    context = {'project':projectObj}
    return render(request,'projects/single_project.html',context)