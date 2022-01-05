
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

    # skilss
    path('create_skill/', views.create_skill,name='create_skill'),
    path('edit_skill/<str:pk>/', views.edit_skill,name='edit_skill'),
    path('delete_skill/<str:pk>/', views.delete_skill,name='delete_skill'),
    
    # message
    path('inbox/', views.my_inbox, name="inbox"),
    path('create-message/<str:pk>/', views.create_message, name="create_message"),
    path('message/<str:pk>/', views.check_message, name="message"),
]
