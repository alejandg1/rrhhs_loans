
from django.forms import ModelForm
from apps.loans.models import Payment


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
