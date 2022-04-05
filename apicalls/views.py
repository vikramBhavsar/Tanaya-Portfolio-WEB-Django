from ast import Delete
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import viewsets, permissions, mixins, generics
from .serializers import ProjectSerializer, MediaContentSerializer, SectionSerializer,ProjectMainSerializer
from .models import MediaContent, Project,Section

# Create your views here.
def index(request):
    return HttpResponse("hello World")

# CRUD operation for Project models
class ProjectAPICRUD(generics.ListAPIView, mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    # for Creating a new project
    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)

    # for updating an existing project
    def put(self, request, *args, **kwargs):
        return self.update(request,*args,**kwargs)

    # for deleting an existing project
    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args,**kwargs)

# CRD operation for MediaContent Model
class MediaContentAPICRUD(generics.ListAPIView,mixins.CreateModelMixin, mixins.DestroyModelMixin,mixins.RetrieveModelMixin):
    parser_classes = [MultiPartParser]
    serializer_class = MediaContentSerializer
    queryset = MediaContent.objects.all()

    # getting existing section details
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)

    def delete(self,request, *args, **kwargs):
        return self.destroy(request,*args,**kwargs)

# CRUD operations for Section Model
class SectionAPICRUD(generics.ListAPIView, mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()

    # getting existing section details
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # Creating new project
    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)

    # updating existing project
    def put(self, request, *args, **kwargs):
        return self.update(request,*args,**kwargs)

    # deleting existing project
    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args,**kwargs)

# This view will show all the data combined, includes projects, sections and media content
class AllDataList(generics.ListAPIView,mixins.RetrieveModelMixin):
    queryset = Project.objects.all()
    serializer_class = ProjectMainSerializer


