from django.urls import path
from . import views

urlpatterns = [
    path('', views.certifications, name='certifications'),  
    path('add-cert', views.add_cert, name="add_cert"),
    path('update-cert/<int:pk>', views.update_cert, name="update_cert"),
    path('delete-cert/<int:pk>', views.delete_cert, name="delete_cert"),
]