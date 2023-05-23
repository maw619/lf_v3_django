from django.urls import path
from . import views

urlpatterns = [
    path('',views.reports, name="reports"),
    path('add-report', views.add_report, name="add_report"),
    path('update-report/<int:pk>', views.update_report, name="update_report"),
    path('delete-report/<int:pk>', views.delete_report, name="delete_report"),
    path('add-photo/<int:pk>', views.add_photo, name="add_photo"),
    path('add-photo2/<int:pk>/<int:ph1_id>', views.add_photo2, name="add_photo2"),
    path('detailed-report/<int:pk>', views.detailed_report, name="detailed_report"),
    path('delete-photo/<int:pk>', views.delete_photo, name="delete_photo"),
    path('delete-photo2/<int:pk>', views.delete_photo2, name="delete_photo2"),
    path('update-photo1/<int:pk>', views.update_photo1, name="update_photo1"),
    path('update-photo2/<int:pk>', views.update_photo2, name="update_photo2"),
]
