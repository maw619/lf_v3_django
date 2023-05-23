from django import forms
from base.models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['pr_desc','pr_address']

        widgets = {
            'pr_desc': forms.TextInput(attrs={'class': 'form-control'}),
            'pr_address': forms.TextInput(attrs={'class': 'form-control'}),
        }
