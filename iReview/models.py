from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='media')
    bio = models.TextField()
    projects = models.ForeignKey()
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()   


class Rating(models.Model):
    name = models.CharField(max_length=30)    