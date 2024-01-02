from django import forms
from django.forms import ModelForm
from apps.loans.models import Payment


class PaymentForm(ModelForm):
    payment_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    payment_date_descount = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    class Meta:
        model = Payment
        fields = '__all__'
        
    def clean(self):
        cleaned_data = super().clean()
        payment_date = cleaned_data.get('Fecha de pago')
        payment_date_descount = cleaned_data.get('payment_date_descount')

        if payment_date and payment_date_descount:
            if payment_date_descount < payment_date:
                msg = 'La fecha de inicio de descuento no puede ser anterior a la fecha del préstamo.'
                self.add_error('Fecha de descuento', msg)

        return cleaned_data
