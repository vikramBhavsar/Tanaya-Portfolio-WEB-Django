from django.urls import path

from . import views

urlpatterns = [
    path('projects',views.ProjectList.as_view(),name='projects'),
    path('project/<pk>',views.ProjectList.as_view(),name='project'),
    path('', views.index, name='index'),
]
