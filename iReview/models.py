from django.db import models

# Create your models here.


class Profile(models.Model):
    profile_photo = models.ImageField(null=True)
    bio = models.CharField(max_length=200, blank=True)
    projects = models.ForeignKey()