from django import forms
from base.models import Certifications

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certifications
        fields = ['cer_desc']

        widgets = {
            'cer_desc': forms.TextInput(attrs={'class':'form-control'})
        }