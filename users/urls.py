
"""users app url handlers"""

from django.contrib import admin
from  django.urls import path 

from . import views
urlpatterns = [
    path('', views.profiles,name='profiles'),
    # path('profiles/', views.profiles,name='profiles'),
    # path('profiles/', views.profiles,name='profiles'),
]
