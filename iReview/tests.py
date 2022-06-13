from django.test import TestCase
from django.contrib.auth.models import User
from .models import *

# Create your tests here.

class ProjectTestCase(TestCase):

    def setUp(self):
        """
        Create a project for testing
        """
        self.user=User(username='tildah',email='teetee@gmail.com',password='Access')
        self.project=Project(image='webinar.jpg',title='website',description='includes the new design trend',url='https.recommend.com',rate=6,user=self.user)
        self.rate=Rating(project=self.project,user=self.user,content=5,usability=6,design=5,average_rate=7)

    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))
        self.assertTrue(isinstance(self.project,Project))
        self.assertTrue(isinstance(self.rate,Rating))

    def test_save(self):
        self.user.save()
        self.project.save_project()
        self.rate.save_rating()    
