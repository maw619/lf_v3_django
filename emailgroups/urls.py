from django.urls import path
from . import views

urlpatterns = [
    path('', views.email_groups, name='email_groups'),
    path('delete_email_group/<str:pk>/', views.delete_email_group, name='delete_email_group'),
    path('update-email-group/<str:pk>/', views.update_email_group, name='update_email_group'),
]