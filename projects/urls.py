from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('project/<str:pk>/', views.single_project, name='project'),
    path('create-project/', views.create_project, name='create-project'),
    path('edit-project/<str:pk>/', views.edit_project, name='edit-project'),
    path('delete-project/<str:pk>/', views.delete_project, name='delete-project')
]
