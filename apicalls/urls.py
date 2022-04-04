from django.urls import path

from . import views

urlpatterns = [
    path('all-projects',views.ProjectList.as_view(),name='all-projects'),
    path('', views.index, name='index'),
]