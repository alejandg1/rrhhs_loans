from django.urls import reverse_lazy
from apps.loans.models import Insurance
from apps.loans.forms.insurance import InsuranceForm

from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.db.models import Q

from apps.security.mixins.mixins import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin, PermissionMixin


class InsuranceListView(PermissionMixin, ListViewMixin, ListView):
    model = Insurance
    template_name = 'insurance/list.html'
    context_object_name = 'insurances'

    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get('q1')  # ver
        if q1 is not None:
            self.query.add(Q(insurier__icontains=q1), Q.AND)
        # q2 = self.request.GET.get('q2') # ver
        # if q2 is not None:
        #     query.add(Q(estado__icontains=q2), Q.AND)
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'seguros'
        context['create_url'] = reverse_lazy('loans:insurance_create')
        return context


class InsuranceCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = Insurance
    template_name = 'insurance/form.html'
    form_class = InsuranceForm
    success_url = reverse_lazy('loans:insurance_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Ingresar nuevo seguro'
        context['grabar'] = 'Grabar seguro'
        context['back_url'] = self.success_url
        return context


class InsuranceUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = Insurance
    template_name = 'insurance/form.html'
    form_class = InsuranceForm
    success_url = reverse_lazy('loans:insurance_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Actualizar el seguro'
        context['grabar'] = 'Actualizar seguro'
        context['back_url'] = self.success_url
        return context


class InsuranceDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = Insurance
    template_name = 'insurance/delete.html'
    success_url = reverse_lazy('loans:insurance_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Eliminar el seguro'
        context['grabar'] = 'Eliminar seguro'
        context['description'] = f"¿Desea Eliminar la seguro: {self.object.name}?"
        context['back_url'] = self.success_url
        return context
