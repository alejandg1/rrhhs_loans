from django import forms
from django.forms import ModelForm
from apps.loans.models import Employee, ESTADO_CHOICES

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        exclude = ['date_entry']
        
    state = forms.ChoiceField(
        choices=ESTADO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )