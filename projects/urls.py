from django.urls import path
from . import views


urlpatterns = [
    path('', views.projects, name='projects'),
    path('add-project', views.add_project, name='add_project'),
    path('update-project/<str:pk>', views.update_project, name='update_project'),
    path('delete-project/<str:pk>', views.delete_project, name='delete_project'),
]