from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save



# Create your models here.


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='media',null= True)
    bio = models.TextField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    contact = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()   

    def delete_profile(self):
        self.delete()
        



class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project')
    title = models.CharField(max_length=75)
    image = models.ImageField(upload_to='photos')
    description = models.TextField()
    url = models.URLField()
    posted = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(default=0)

    def __str__(self):
        return  self.title

    def save_project(self):
        self.save()  

    def delete_project(self):
        self.delete()    


class Rating(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,null=False)
    design = models.IntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(10)])
    content = models.IntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(10)])
    usability = models.IntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(10)])
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    average_rate = models.IntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(10)])

    def __str__(self):
        return self.content

    def save_rating(self):
        self.save() 

    def delete_rating(self):
        self.delete()        


