from datetime import datetime
from django.test import TestCase
import unittest
from unittest.mock import patch

# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from projects.models import Project, Review, Tag

from users.models import Profile


class TestProject(TestCase):
    """ Tests project model has expected fields and corresponding table columns exists.
    """
    #A.A.A ---- > Arrange,action,assert
    
    @classmethod
    def setUpTestData(cls):
        # USER
        cls.user1 = User(username='admin1',email='admin@fe2.com')
        cls.user1.is_superuser = True
        cls.user1.is_staff = True
        cls.user1.set_password('adminpass')
        cls.user1.save()

        #Profile
        # cls.profile = Profile.objects.create(
        #     user=cls.user1,
        #     email=cls.user1.email,
        #     )

        cls.project = Project.objects.create(
        title="project1",
        description="a project that reads from a script.",
        demo_link="https://somelink.com",
        source_link="",
        vote_total=3,
        vote_ratio=4)
         
    def setUp(self):
       self.client.login(username=self.user1.username,password='adminpass') 

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count,1)
        self.assertNotEqual(user_count,0)

    def test_project_correct_data(self):
        self.assertIsInstance(self.project.title, str)
        self.assertIsInstance(self.project.description, str)
        self.assertNotIsInstance(self.project.vote_ratio, str)
        self.assertIsInstance(self.project.vote_ratio, int)
        
    def test_project_has_timestamps(self):
        self.assertIsInstance(self.project.created, datetime)

    def test_string_representation(self):
        self.assertEqual(self.project.__str__(),self.project.title)

    def test_project_can_have_multiple_tags(self):
        tag_names = ['django','python','html'] 
        model_tags = [Tag.objects.create() for _ in tag_names]
        for tag in model_tags:
            self.project.tags.add(tag) 
        self.assertEqual(len(model_tags), self.project.tags.count())

    def test_review_query(self):
        Review.objects.create(value='Up Vote',project=self.project)
        rev = Review.objects.get(value='Up Vote')
        self.assertEqual(rev.value, 'Up Vote')

    def test_vote_counts_calc(self):
        Review.objects.create(value='Up Vote',project=self.project)

        up_vote = Review.objects.filter(value='Up Vote').count()
        total_votes = Review.objects.all().count()

        ratio = (up_vote / total_votes) * 100
        self.project.vote_total = total_votes
        self.project.vote_ratio = ratio
        self.project.save()
        self.assertEqual(up_vote,1)        
        self.assertEqual(total_votes,1)        
        self.assertEqual(ratio,100.0)
        self.assertEqual(self.project.vote_total,total_votes)        
        self.assertEqual(self.project.vote_ratio,ratio)
      

        
   
             

class TestReview(TestCase):
    pass

class TestTag(TestCase):
    pass