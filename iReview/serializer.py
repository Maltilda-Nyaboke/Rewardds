from rest_framework import serializers
from .models import Profile,Project


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_photo','bio','user','contact')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['user','title','image','description','url','posted','rate']
