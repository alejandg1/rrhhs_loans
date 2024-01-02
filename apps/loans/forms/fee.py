from django import forms
from django.forms import ModelForm
from apps.loans.models import Fee


class FeeForm(ModelForm):
    payment_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    ) 
    class Meta:
        model = Fee
        fields = ['payment_date']
