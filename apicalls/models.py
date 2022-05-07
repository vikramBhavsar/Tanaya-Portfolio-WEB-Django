from distutils.command.upload import upload
from django.db import models
from datetime import datetime
from django.utils import timezone
import os


# Create your models here.
def update_project_filename(instance, filename):
    ext = filename.split('.')[-1]
    path = "Images/"
    format = 'img_' + datetime.now().strftime('%H_%M_%S_%f') +'.'+ ext
    return os.path.join(path, format)

class Project(models.Model):
    projectName = models.CharField(max_length=1000)
    projectDescription = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.projectName + str(self.pk)

class Section(models.Model):
    sectionName = models.CharField(max_length=1000)
    sectionDescription = models.TextField(blank=True)
    sectionDisplayType = models.CharField(max_length=10,blank=True)
    projectID = models.ForeignKey(Project, on_delete=models.CASCADE,related_name='sections')

    def __str__(self) -> str:
        return self.sectionName + str(self.projectID)

class MediaContent(models.Model):
    mediaDescription = models.CharField(max_length=1000,blank=True)
    isVideo = models.BooleanField(default=False)
    mediaFile = models.ImageField(upload_to=update_project_filename,blank=True)
    videoUrl = models.TextField(default="")
    sectionID = models.ForeignKey(Section,on_delete=models.CASCADE,related_name="mediaContent")




####### For Art Education #####
##### BELOW MODELS ARE FOR ART EDUCATION #####
def update_media_filename(instance, filename):
    ext = filename.split('.')[-1]
    path = "artImages/"
    format = 'img_' + datetime.now().strftime('%H_%M_%S_%f') +'.'+ ext
    return os.path.join(path, format)


class ArtProject(models.Model):
    projectName = models.CharField(max_length=1000)
    projectDescription = models.TextField(blank=True)
    projectDisplayType = models.CharField(max_length=10,blank=True)

    def __str__(self) -> str:
        return self.projectName

class ArtMediaContent(models.Model):
    mediaDescription = models.CharField(max_length=1000,blank=True)
    isVideo = models.BooleanField(default=False)
    mediaFile = models.ImageField(upload_to=update_media_filename,blank=True)
    videoUrl = models.TextField(default="",blank=True)
    projectID = models.ForeignKey(ArtProject,on_delete=models.CASCADE,related_name="art_media")





######### FOR BLOGGING ######
######### below models are for blogging #######


def update_blog_filename(instance, filename):

    ext = filename.split('.')[-1]
    path = "blog/"
    format = 'img_' + datetime.now().strftime('%H_%M_%S_%f') +'.'+ ext
    return os.path.join(path, format)


class Blog(models.Model):
    blogName = models.CharField(max_length=1000)
    isPublished = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.blogName


class BlogSection(models.Model):
    blogID = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='blog_sections')
    sectionType = models.CharField(max_length=5,default='T')
    sectionText = models.TextField(blank=True)
    mediaURL = models.ImageField(upload_to=update_blog_filename,blank=True)
    mediaDes= models.CharField(max_length=500,blank=True)
    videoURL = models.TextField(default="",blank=True)
    timestamp = models.DateTimeField(default=timezone.now())

    def __str__(self) -> str:
        return self.sectionText[:10] + '.. ' + str(self.pk)

    class Meta:
        ordering = ['pk','timestamp']


    '''
    Section type for this model defines type of content inside the section:
    'T'  - text content
    'I'  - single image content
    'V'  - single Video Content
    'MI' - Multiple Image content
    'MV' - Multiple Video content
    '''

## Below model is if the user upload multiple images to the section
class MediaGroupSection(models.Model):
    BlogSectionID = models.ForeignKey(BlogSection, on_delete=models.CASCADE,related_name='media_group_section')
    mediaURL = models.ImageField(upload_to='blogs/%H_%M_%S_%f',blank=True)
    mediaDes= models.CharField(max_length=500,blank=True)


def update_about_filename(instance, filename):
    ext = filename.split('.')[-1]
    path = "about/"
    format = 'img_' + datetime.now().strftime('%H_%M_%S_%f') +'.'+ ext
    return os.path.join(path, format)

class About(models.Model):
    about_heading = models.CharField(max_length=200,blank=True)
    about_content =  models.TextField(max_length=1000,blank=True)
    mediaFile = models.ImageField(upload_to=update_about_filename,blank=True)

    def __str__(self) -> str:
        return str(self.pk) + ' ' + self.about_heading
    
