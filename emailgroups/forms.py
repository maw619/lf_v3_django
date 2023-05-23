from django import forms
from base.models import EmailGroup 
from base.models import Employee

class AddEmailGroupForm(forms.ModelForm):
        class Meta:
            model = EmailGroup
            fields = {'name','members'}
            fields_order = ['name','members']
            # labels = {
            #     'name': 'Group Name',
            #     'members': 'members email'
            # }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            # 'members': forms.ModelMultipleChoiceField(queryset=Employee.objects.all(),
            #                                      widget=forms.SelectMultiple(attrs={'class': 'select2','id':'js-example-basic-hide-search-multi'}))
            'members': forms.SelectMultiple(attrs={'class': 'form-select', 'multiple': 'multiple'}),
        }