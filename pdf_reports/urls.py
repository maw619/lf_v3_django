from django.urls import path
from . import views

urlpatterns = [
    path('report_pdf/<int:pk>', views.report_pdf, name='report_pdf'), 
]