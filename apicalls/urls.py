from django.urls import path

from . import views

urlpatterns = [
    path('projects',views.ProjectAPICRUD.as_view(),name='projects'),
    path('project/<pk>',views.ProjectAPICRUD.as_view(),name='project'),
    path('media',views.MediaContentAPICRUD.as_view(),name='media-content'),
    path('all-projects-detail',views.AllDataList.as_view(),name='all-projects-detail'),
    path('', views.index, name='index'),
]
