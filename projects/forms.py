from django.forms import ModelForm
from .models import Project, Review, Tag


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'