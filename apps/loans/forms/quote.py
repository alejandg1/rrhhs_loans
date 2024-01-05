from django.forms import ModelForm
from apps.loans.models import Quote


class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = ['payment_date', 'amount', 'state']
