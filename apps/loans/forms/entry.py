from django.forms import ModelForm
from apps.loans.models import Entry


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['code', 'description', 'value']
