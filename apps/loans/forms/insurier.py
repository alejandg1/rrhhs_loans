from django.forms import ModelForm
from apps.loans.models import Insurier


class InsurierForm(ModelForm):
    class Meta:
        model = Insurier
        fields = ['name', 'tlf_contact', 'state']
