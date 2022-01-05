from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile, Skills, Message

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields =  ('first_name','email', 'username',  'password1', 'password2')
        labels = {'first_name': 'Name', 'email':'Email'}

    def __init__(self, *args, **kwargs):
        """ override init and modify/update project form fields. """
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'username','location','bio','short_intro','profile_image','social_github','social_twitter','social_linkedin','social_youtube','social_website')

    def __init__(self, *args, **kwargs):
        """ override init and modify/update project form fields. """
        super(ProfileForm,self).__init__(*args, **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'}) 
        

class SkillForm(ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'
        exclude = ['owner']
        
    def __init__(self, *args, **kwargs):
        """ override init and modify/update project form fields. """
        super(SkillForm, self).__init__(*args, **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name','email','subject','body']
       
        
    def __init__(self, *args, **kwargs):
        """ override init and modify/update project form fields. """
        super(MessageForm, self).__init__(*args, **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'}) 