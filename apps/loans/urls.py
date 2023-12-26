from django.urls import path
from apps.loans.views import insurance, insurier, employee, entry
app_name = "loans"
urlpatterns = []
# urls de las vistas de organizacion
urlpatterns += [
     # insurier
     path('insurier/list',
          insurier.InsurierListView.as_view(),
          name="insurier_list"),
     path('insurier/create',
          insurier.InsurierCreateView.as_view(),
          name="insurier_create"),
     path('insurier/update/<int:pk>',
          insurier.InsurierUpdateView.as_view(),
          name="insurier_update"),
     path('insurier/delete/<int:pk>',
          insurier.InsurierDeleteView.as_view(),
          name="insurier_delete"),
     # insurance
     path('insurance/list',
          insurance.InsuranceListView.as_view(),
          name="insurance_list"),
     path('insurance/create',
          insurance.InsuranceCreateView.as_view(),
          name="insurance_create"),
     path('insurance/update/<int:pk>',
          insurance.InsuranceUpdateView.as_view(),
          name="insurance_update"),
     path('insurance/delete/<int:pk>',
          insurance.InsuranceDeleteView.as_view(),
          name="insurance_delete"),
     # employee
          path('employee/list',
          employee.EmployeeListView.as_view(),
          name="employee_list"),
     path('employee/create',
          employee.EmployeeCreateView.as_view(),
          name="employeee_create"),
     path('employee/update/<int:pk>',
          employee.EmployeeUpdateView.as_view(),
          name="employee_update"),
     path('employee/delete/<int:pk>',
          employee.EmployeeDeleteView.as_view(),
          name="employee_delete"),
     # entry
          path('entry/list',
          entry.EntryListView.as_view(),
          name="entry_list"),
     path('entry/create',
          entry.EntryCreateView.as_view(),
          name="entry_create"),
     path('entry/update/<int:pk>',
          entry.EntryUpdateView.as_view(),
          name="entry_update"),
     path('entry/delete/<int:pk>',
          entry.EntryDeleteView.as_view(),
          name="entry_delete"),
     ]
