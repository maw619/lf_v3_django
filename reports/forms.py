from django import forms
from base.models import Report, Photo, Photo2

class AddReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['employee','project','supervisors','rep_desc','rep_notes']
        exclude = ['id']    

        widgets = {
            'employee' : forms.Select(attrs={'class':'form-control'}),
            'project' : forms.Select(attrs={'class':'form-control'}),
            'supervisors': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'rep_desc': forms.Textarea(attrs={'class':'form-control'}),
            'rep_notes': forms.Textarea(attrs={'class':'form-control'}),
            'rep_date': forms.HiddenInput(),
            'rep_user_name': forms.HiddenInput()
        }

class AddPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['ph_link','ph_desc','ph_desc','ph_user_name','ph_observation','reports']
        exclude = ['reports','ph_date']
        widgets = {
            'ph_link': forms.ClearableFileInput(attrs={'class':'form-control', 'required':False}),
            'ph_desc': forms.TextInput(attrs={'class':'form-control'}),
            'ph_observation': forms.Textarea(attrs={'class':'form-control'}), 
            'ph_user_name': forms.HiddenInput(),
             
        }

class AddPhotoForm2(forms.ModelForm):
    class Meta:
        model = Photo2
        fields = ['ph_link2','ph_desc2','ph_desc2','ph_observation2','reports2']
        exclude = ['reports2','ph_date2']
        widgets = {
            'ph_link2': forms.ClearableFileInput(attrs={'class':'form-control', 'required':False}),
            'ph_desc2': forms.TextInput(attrs={'class':'form-control'}),
            'ph_observation2': forms.Textarea(attrs={'class':'form-control'}),  
        }