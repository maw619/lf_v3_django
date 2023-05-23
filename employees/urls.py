from django.urls import path
from . import views

urlpatterns = [
    path('', views.employees, name='employees'),
    path('<int:pk>', views.employee_info, name='employee_info'),
    path('add-employee', views.add_employee, name="add_employee"),
    path('update-employee/<int:pk>', views.update_employee, name="update_employee"),
    path('delete-employee/<int:pk>', views.delete_employee, name="delete_employee"),
    
]