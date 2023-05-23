from django import forms
from base.models import Charges


class ChargesForm(forms.ModelForm):
    class Meta:
        model = Charges
        fields = ['ch_desc']
        widgets = {
            'ch_desc': forms.TextInput(attrs={'class':'form-control'})
        }