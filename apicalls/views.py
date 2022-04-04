from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProjectSerializer, MediaContentSerializer, SectionSerializer,ProjectMainSerializer
from rest_framework import generics
from .models import Project

# Create your views here.
def index(request):
    return HttpResponse("hello World")

# This view will show all the projects
class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# This view will show all the data combined, includes projects, sections and media content.s
class AllDataList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectMainSerializer