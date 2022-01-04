from django.db import models
import uuid
from users.models import Profile
class Project(models.Model):
    owner = models.ForeignKey(Profile,null=True,blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    feature_image = models.ImageField(null=True, blank=True,default='default.jpg')
    demo_link = models.CharField(max_length=2000, blank=True,null=True)
    source_link = models.CharField(max_length=2000,null=True,blank=True)
    tags = models.ManyToManyField('Tag',blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    objects = models.Manager() # provides interface between db query operations and the django model.


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


class Review(models.Model):
    VOTE_TYPE = (
        ('up','Up Vote'),
        ('down','Down Vote')
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    
    objects = models.Manager() # provides interface between db query operations and the django model.


    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    class Meta:
        """ Ensure that a user can only leave one review per project. 
        By binding owner and project values so no instance of a review can have the same owner and the same project.
    """
        unique_together = [['owner','project']]

    def __str__(self):
        return self.value

class Tag(models.Model):
    name = models.CharField(max_length=200)
    
    objects = models.Manager() # provides interface between db query operations and the django model.

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    def __str__(self):
        return self.name