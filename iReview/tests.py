from django.test import TestCase
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

