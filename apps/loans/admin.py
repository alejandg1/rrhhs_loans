from django.contrib import admin
from apps.loans.models import Entry, Employee, Insurier, Insurance
admin.site.register(Entry)
admin.site.register(Employee)
admin.site.register(Insurance)
admin.site.register(Insurier)

# Register your models here.
