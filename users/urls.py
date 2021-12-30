
"""users app url handlers"""

from django.contrib import admin
from  django.urls import path 

from . import views
urlpatterns = [
    path('', views.profiles,name='profiles'),
    path('profile/<str:pk>/', views.profile,name='my_profile'),
    # path('profiles/', views.profiles,name='profiles'),
]
