from django.contrib import admin
from .models import Employee,  Report, Project, Photo, Photo2, EmailGroup

admin.site.register(Employee)
admin.site.register(Report) 
admin.site.register(Project) 
admin.site.register(Photo)  
admin.site.register(Photo2)
admin.site.register(EmailGroup) 

