from django import forms
from django.forms import ModelForm
from apps.loans.models import Entry, ESTADO_CHOICES


class EntryForm(ModelForm):
    date_prestamo = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    date_descuento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = Entry
        fields = ['id', 'code', 'description', 'value', 'state']

    state = forms.ChoiceField(
        choices=ESTADO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def clean(self):
        cleaned_data = super().clean()
        date_prestamo = cleaned_data.get('date_prestamo')
        date_descuento = cleaned_data.get('date_descuento')

        if date_prestamo and date_descuento:
            if date_descuento < date_prestamo:
                msg = 'La fecha de inicio de descuento no puede ser anterior a la fecha del préstamo.'
                self.add_error('date_descuento', msg)

        return cleaned_data
