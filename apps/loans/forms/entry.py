from django import forms
from django.forms import ModelForm
from apps.loans.models import Entry, ESTADO_CHOICES


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        exclude = ['cuota']

    state = forms.ChoiceField(
        choices=ESTADO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
