from django.db import models
from datetime import datetime


# Create your models here.
class Project(models.Model):
    projectName = models.CharField(max_length=1000)
    projectDate = models.DateField(default=datetime.now().date())
    projectDescription = models.TextField(blank=True)

class Section(models.Model):
    sectionName = models.CharField(max_length=1000)
    sectionDate = models.DateField(default=datetime.now().date())
    sectionDescription = models.TextField(blank=True)
    sectionDisplayType = models.CharField(max_length=10,blank=True)
    projectID = models.ForeignKey(Project, on_delete=models.CASCADE,related_name='sections')

class MediaContent(models.Model):
    mediaDescription = models.CharField(max_length=1000,blank=True)
    mediaDate = models.DateField(default=datetime.now().date())
    isVideo = models.BooleanField(default=False)
    mediaFile = models.ImageField(upload_to="Images")
    videoUrl = models.TextField(default="")
    sectionID = models.ForeignKey(Section,on_delete=models.CASCADE,related_name="mediaContent")