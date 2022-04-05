from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import viewsets, permissions, mixins, generics
from .serializers import ProjectSerializer, MediaContentSerializer, SectionSerializer,ProjectMainSerializer
from .models import Project,Section

# Create your views here.
def index(request):
    return HttpResponse("hello World")

# This view will show all the projects
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
        

class MediaContentAPICRUD(generics.ListAPIView,mixins.CreateModelMixin):
    parser_classes = [MultiPartParser]
    serializer_class = MediaContentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)
        
    def create(self, request, *args, **kwargs):
        if 'sectionID' in request.data:
            section = Section.objects.filter(pk=request.data['sectionID'])
            print("Following Section found %s" % section)
        
        # return Response("Yo dumbass")
        return super().create(request, *args, **kwargs)

# This view will show all the data combined, includes projects, sections and media content.s
class AllDataList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectMainSerializer
