from django.db import models
from django.contrib.auth.models import User


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


class Rating(models.Model):
    design = models.IntegerField(default=0)
    content = models.IntegerField(default=0)
    usability = models.ForeignKey(default=0)

    def __str__(self):
        return self.content

    def save_rating(self):
        self.save()     

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


