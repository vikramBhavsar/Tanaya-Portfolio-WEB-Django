from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Project,Section,MediaContent

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"

class MediaContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaContent
        fields = "__all__"    

class SectionMainSerializer(serializers.ModelSerializer):
    mediaContent = MediaContentSerializer(many=True,read_only=True)

    class Meta:
        model = Section
        fields = "__all__"


class ProjectMainSerializer(serializers.ModelSerializer):

    sections = SectionMainSerializer(many=True,read_only=True)

    class Meta:
        model = Project
        fields = "__all__"