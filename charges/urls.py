from django.urls import path
from . import views

urlpatterns = [
    path('', views.charges, name='charges'), 
    path('add-charge', views.add_charge, name="add_charge"),
    path('update-charge/<int:pk>', views.update_charge, name="update_charge"),
    path('delete-charge/<int:pk>', views.delete_charge, name="delete_charge")
]