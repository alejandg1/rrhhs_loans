from django.forms import ModelForm
from apps.loans.models import Fee


class FeeForm(ModelForm):
    class Meta:
        model = Fee
        fields = ['payment_date']
