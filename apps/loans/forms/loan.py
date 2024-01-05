from django.forms import ModelForm
from apps.loans.models import Loan


class LoanForm(ModelForm):
    class Meta:
        model = Loan
        fields = '__all__'
