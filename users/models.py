from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
import uuid

from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(max_length=500,blank=True,null=True)
    username = models.CharField(max_length=200,blank=True,null=True)
    location = models.CharField(max_length=200,blank=True,null=True)
    short_intro = models.CharField(max_length=500,blank=True,null=True)
    bio = models.TextField(blank=True,null=True)
    profile_image = models.ImageField(null=True,blank=True, upload_to='profiles/',default='profiles/user-default.png')
    social_github = models.CharField(max_length=200,blank=True,null=True)
    social_twitter = models.CharField(max_length=200,blank=True,null=True)
    social_linkedin = models.CharField(max_length=200,blank=True,null=True)
    social_youtube = models.CharField(max_length=200,blank=True,null=True)
    social_website = models.CharField(max_length=200,blank=True,null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    objects = models.Manager() # provides interface between db query operations and the django model.

    def __str__(self):
        return str(self.username)



class Skills(models.Model):
    owner = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True,blank=True)
    skill_name = models.CharField(max_length=200,blank=True,null=True)
    skill_description = models.TextField(blank=True,null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    objects = models.Manager() # provides interface between db query operations and the django model.

    def __str__(self):
        return str(self.skill_name)
    
    
class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="messages") #To access the profiles messages instead of doing something like profile.message_set()
    name = models.CharField(max_length=200, blank=True,null=True)
    email = models.EmailField(max_length=200, blank=True,null=True)
    subject = models.CharField(max_length=200, blank=True,null=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    
    objects = models.Manager() # provides interface between db query operations and the django model.

    class Meta:
        """Ensure all unread messages are on the top."""
        ordering = ['is_read','-created'] #all false value will be on top
    
    def __str__(self):
        return str(self.subject)

   
        
    
 