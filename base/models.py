from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User


class Employee(models.Model):
    name = models.CharField(max_length=70, blank=True, null=True)
    cargo = models.ForeignKey('Cargo', on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'employees'

    def __str__(self) -> str:
        return self.name
 

class Report(models.Model): 
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='reports_as_employee')
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    supervisors = models.ManyToManyField('Employee', related_name='reports_as_supervisor')
    rep_desc = models.CharField(max_length=255, blank=True, null=True)
    rep_user_name = models.CharField(max_length=50, blank=True, null=True)
    rep_notes = models.CharField(max_length=255, blank=True, null=True)
    rep_date = models.DateField(default=timezone.now) 

  
    def __str__(self):
        return f"{self.rep_user_name}, {self.rep_desc}, {self.rep_date}"

    class Meta:
        db_table = 'reportes'


 
class Project(models.Model):
    pr_desc = models.CharField(max_length=150, blank=True, null=True)
    pr_address = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'projects'

    def __str__(self) -> str:
        return self.pr_desc


class Cargo(models.Model):
    desc = models.CharField(max_length=50, blank=True, null=True) 
    class Meta:
        managed = True
        db_table = 'cargos' 
    def __str__(self) -> str:
        return self.desc
    

class Photo(models.Model): 
    ph_link = models.ImageField(upload_to='images/',null=True, blank=True)
    ph_date = models.DateField(default=timezone.now) 
    ph_desc = models.CharField(max_length=999, blank=True, null=True)
    ph_user_name = models.CharField(max_length=50, blank=True, null=True)
    ph_observation = models.CharField(max_length=5000, blank=True, null=True) 
    reports = models.ForeignKey('Report', on_delete=models.CASCADE, null=True)
    
    class Meta:
        managed = True
        db_table = 'photos'
    def __str__(self) -> str:
        return f"{self.ph_link}"


class Photo2(models.Model): 
    ph_link2 = models.ImageField(upload_to='images2/',null=True, blank=True)
    ph_date2 = models.DateField(default=timezone.now) 
    ph_desc2 = models.CharField(max_length=999, blank=True, null=True) 
    ph_observation2 = models.CharField(max_length=5000, blank=True, null=True) 
    reports2 = models.ForeignKey('Report', on_delete=models.CASCADE, null=True)
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE, null=True)


    class Meta:
        managed = True
        db_table = 'photos2'
    def __str__(self) -> str:
        return f"{self.ph_link2}"
    

class Certifications(models.Model): 
    cer_desc = models.CharField(max_length=50, blank=True, null=True) 
    class Meta:
        managed = True
        db_table = 'certifications'
    def __str__(self) -> str:
        return self.cer_desc

class Charges(models.Model): 
    ch_desc = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'charges'
    def __str__(self) -> str:
        return self.ch_desc
    


class EmailGroup(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField('Employee', related_name='email_groups')

    def __str__(self):
        return self.name

