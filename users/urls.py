
"""users app url handlers"""

from django.contrib import admin
from  django.urls import path 

from . import views
urlpatterns = [
    path('', views.profiles,name='profiles'),
    path('profile/<str:pk>/', views.profile,name='my_profile'),


    # authentication
    path('register/', views.register_user,name='register'),
    path('login/', views.login_user,name='login'),
    path('logout/', views.logout_user,name='logout'),

    # Account
    path('account/', views.user_account,name='account'),
    path('edit_account/', views.edit_account,name='edit_account'),
    # path('/', views.,name=''),
    # path('/', views.,name=''),
    # path('/', views.,name=''),
    
    
]
