from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile

from django.core.mail import send_mail
from django.conf import settings

def create_profile(sender,created,instance, **kwargs):
    """create profile automatically when a user is created.
        Args:
            sender ([User]): User notifies this function that a new user being created in db
            created ([Bool]): If User does NOT exists,create profile. created = True
            instance ([User]): new user associated with the profile.
    """
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email = user.email,
            name=user.first_name,
            )
        subject = 'Welcome to DevSearch'
        message = 'We are glad you are here!'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER, #sender
            [profile.email],#recipient
            fail_silently=False,
)



def update_user_account(sender,created,instance, **kwargs):
    """ Update and save profile.

    Args:
        sender ([Profile]): [anytime Profile is updated,this function gets triggered]
        created ([Bool]): If User already exists,update profile. created = False
        instance ([Profile]): current profile.
    """
    profile = instance
    user = profile.user
    #validate created == false to avoid recursion error
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()
        

def delete_profile(sender,instance, **kwargs):
    """ delete User when profile is deleted

    Args:
        sender ([Profile]): [description]
        created ([Bool]): If User exists, delete profile. created = False
        instance ([User]): current user associated with the profile.
    """
    try:
        user = instance.user
        user.delete()
    except:
        print('Error: Unable to delete user')

post_save.connect(create_profile, sender=User)
post_save.connect(update_user_account, sender=Profile)
post_delete.connect(delete_profile, sender=Profile)