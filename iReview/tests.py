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

        users = User.objects.all()
        projects = Project.objects.all()
        rates = Rating.objects.all()
        
        self.assertTrue(len(projects) > 0)
        self.assertTrue(len(users) > 0)
        self.assertTrue(len(rates) > 0)

    def test_update(self):
        self.user.save()
        self.project.save_project()   

    def test_delete(self):
        self.user.delete()
        self.project.delete_project()
        self.rate.delete_rating()


        Rating.objects.get(id =self.rate.id).delete()
        Project.objects.get(id =self.project.id).delete()
        User.objects.get(id =self.user.id).delete()
        rates=Rating.objects.all()
        projects=Project.objects.all()

        users=User.objects.all()
        self.assertTrue(len(rates) == 0)
        self.assertTrue(len(users) == 0)
        self.assertTrue(len(projects) == 0)
