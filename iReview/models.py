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
    design = models.ForeignKey
    content = models.ForeignKey
    usability = models.ForeignKey 

class Project(models.Model):
          