from django.forms import ModelForm
from django import forms
from .models import Project, Review, Tag


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','feature_image','description', 'demo_link','source_link','tags']

        widgets ={
            'tags':forms.CheckboxSelectMultiple(),
        }
    def __init__(self, *args, **kwargs):
        """ override init and modify/update project form fields. """
        super(ProjectForm, self).__init__(*args, **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
     

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value','body']
        labels = {
            'value':'Place you vote',
            'body':'Leave a comment with your vote'
        }

        widgets ={
            'tags':forms.CheckboxSelectMultiple(),
        }
    def __init__(self, *args, **kwargs):
        """ override init and modify/update project form fields. 
        By looping through all the fields and adding in the class of input """
        super(ReviewForm, self).__init__(*args, **kwargs)
        for name,field in self.fields.items():
            # and this going to allow it to be styled with css theme
            field.widget.attrs.update({'class':'input'}) 
        
        