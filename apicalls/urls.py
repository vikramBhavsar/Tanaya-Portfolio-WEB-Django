from django.urls import path

from . import views

urlpatterns = [
    # For Project related manipulation
    path('projects',views.ProjectAPICRUD.as_view(),name='projects'),
    path('project/<pk>',views.ProjectAPICRUD.as_view(),name='project'),

    # for Section Related manipulation
    path('section',views.SectionAPICRUD.as_view(),name='section'),
    path('section/<pk>',views.SectionAPICRUD.as_view(),name='section'),

    # for Media related manipulation
    path('media',views.MediaContentAPICRUD.as_view(),name='media-content'),
    path('media/<pk>',views.MediaContentAPICRUD.as_view(),name='media-content'),

    
    path('all-projects-detail',views.AllDataList.as_view(),name='all-projects-detail'),
    path('', views.index, name='index'),
]
