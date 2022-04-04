from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, permissions, mixins, generics
from .serializers import ProjectSerializer, MediaContentSerializer, SectionSerializer,ProjectMainSerializer
from .models import Project

# Create your views here.
def index(request):
    return HttpResponse("hello World")

# This view will show all the projects
class ProjectList(generics.ListAPIView, mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin):
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


# This view will show all the data combined, includes projects, sections and media content.s
class AllDataList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectMainSerializer