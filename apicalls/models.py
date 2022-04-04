from django.db import models
from datetime import datetime

# Create your models here.
class Project(models.Model):
    projectName = models.CharField(max_length=1000)
    projectDate = models.DateField(default=datetime.now())
    projectDescription = models.TextField()

class Section(models.Model):
    sectionName = models.CharField(max_length=1000)
    sectionDate = models.DateField(default=datetime.now())
    sectionDescription = models.TextField()
    sectionDisplayType = models.CharField(max_length=10)
    projectID = models.ForeignKey(Project, on_delete=models.CASCADE,related_name='sections')

class MediaContent(models.Model):
    mediaDescription = models.CharField(max_length=1000)
    mediaDate = models.DateField(default=datetime.now())
    isVideo = models.BooleanField(default=False)
    mediaFile = models.ImageField(upload_to="Images")
    videoUrl = models.TextField(default="")
    sectionID = models.ForeignKey(Section,on_delete=models.CASCADE,related_name="mediaContent")