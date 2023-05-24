from django import forms
from base.models import Employee

class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name','charge','email','phone']
        exclude = ['id']
        labels = {'name':'Name', 'charge':'Charge', 'email':'Email', 'phone':'Phone'}

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'charge': forms.Select(attrs={'class':'form-control'})
        }