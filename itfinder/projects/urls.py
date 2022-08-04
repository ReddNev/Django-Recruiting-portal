from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('project/<slug:project_slug>/', views.project, name="project"),
    path('tag/<slug:tag_slug>', views.projects_by_tag, name="tag"),
    path('create-project/', views.create_project, name="create-project"),
    path('update-project/<str:pk>', views.update_project, name="update-project"),
    path('delete-project/<str:pk>', views.delete_project, name="delete-project"),
]