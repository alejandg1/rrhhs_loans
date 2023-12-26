from django.contrib import admin
from apps.loans.models import entry, employee, Insurier, Insurance
admin.site.register(entry)
admin.site.register(employee)
admin.site.register(Insurance)
admin.site.register(Insurier)

# Register your models here.
