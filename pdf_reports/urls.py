from django.urls import path
from . import views

urlpatterns = [
    path('report_pdf/<int:pk>', views.report_pdf, name='report_pdf'), 
    path('report_pdf_download/<int:pk>', views.report_pdf_download, name='report_pdf_download'), 
]