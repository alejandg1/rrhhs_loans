from django.forms import ModelForm
from apps.loans.models import Insurance


class InsuranceForm(ModelForm):
    class Meta:
        model = Insurance
        fields = ['insurier', 'employee']
