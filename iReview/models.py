from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save



# Create your models here.


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='media')
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    contact = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()   

    def delete_profile(self):
        self.delete()
        

class Rating(models.Model):
    design = models.IntegerField(default=0,validators=[])
    content = models.IntegerField(default=0,validators=[])
    usability = models.IntegerField(default=0,validators=[])

    def __str__(self):
        return self.content

    def save_rating(self):
        self.save() 

    def delete_rating(self):
        self.delete()        

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=75, blank=False)
    image = models.ImageField(null= False, blank=False)
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



