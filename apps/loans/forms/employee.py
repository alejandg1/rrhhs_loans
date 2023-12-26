from django.forms import ModelForm
from apps.loans.models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'lastname', 'identity_card',
                  'position', 'department']
