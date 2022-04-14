from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

urlpatterns = [
    # For Project related manipulation
    path('projects',views.ProjectAPICRUD.as_view(),name='projects'),
    path('project/<pk>',views.ProjectAPICRUD.as_view(),name='project-pk'),
    path('all-projects',views.ProjectList.as_view(),name='all-project'),

    # For Section Related manipulation
    path('section',views.SectionAPICRUD.as_view(),name='section'),
    path('section/<pk>',views.SectionAPICRUD.as_view(),name='section'),

    # For Media related manipulation
    path('media',views.MediaContentAPICRUD.as_view(),name='media-content'),
    path('media/<pk>',views.MediaContentAPICRUD.as_view(),name='media-content'),

    
    path('all-projects-detail',views.AllDataList.as_view(),name='all-projects-detail'),
    path('', views.index, name='index'),

    # For Authentication related
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),


]
