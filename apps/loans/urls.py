from django.urls import path
from apps.loans.views import insurance, insurier
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
]
