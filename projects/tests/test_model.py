from datetime import datetime
from django.test import TestCase
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from projects.models import Project, Review, Tag

class TestProject(TestCase):
    """ Tests project model has expected fields and corresponding table columns exists.
    """
    #A.A.A ---- > Arrange,action,assert
    
    @classmethod
    def setUpTestData(cls):
        cls.owner = Project.objects.create(
        title="project1",
        description="a project that reads from a script.",
        demo_link="https://somelink.com",
        source_link="",
        vote_total=3,
        vote_ratio=4)
        
    def setUp(self):
       user1 = User(username='admin1',email='admin@fe2.com')
       user1.is_superuser = True
       user1.is_staff = True
       user1.set_password('adminpass')
       user1.save()

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count,1)
        self.assertNotEqual(user_count,0)

    def test_project_correct_data(self):
        self.assertIsInstance(self.owner.title, str)
        self.assertIsInstance(self.owner.description, str)
        self.assertNotIsInstance(self.owner.vote_ratio, str)
        self.assertIsInstance(self.owner.vote_ratio, int)
        
    def test_project_has_timestamps(self):
        self.assertIsInstance(self.owner.created, datetime)

    def test_string_representation(self):
        self.assertEqual(self.owner.__str__(),self.owner.title)

    def test_project_can_have_multiple_tags(self):
        tag_names = ['django','python','html'] 
        model_tags = [Tag.objects.create() for _ in tag_names]
        for tag in model_tags:
            self.owner.tags.add(tag) 
        self.assertEqual(len(model_tags), self.owner.tags.count())



class TestReview(TestCase):
    pass

class TestTag(TestCase):
    pass