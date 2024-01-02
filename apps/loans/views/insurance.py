from django.urls import reverse_lazy
from apps.loans.models import Insurance
from apps.loans.forms.insurance import InsuranceForm

from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.db.models import Q

from apps.security.mixins.mixins import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin, PermissionMixin


class InsuranceListView(ListViewMixin, ListView):
    model = Insurance
    template_name = 'insurance/list.html'
    context_object_name = 'insurances'
    permission_required = 'view_insurance'

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
        context['permission_add'] = context['permissions'].get(
            'add_insurance', '')
        return context


class InsuranceCreateView(CreateViewMixin, CreateView):
    model = Insurance
    template_name = 'insurance/form.html'
    form_class = InsuranceForm
    success_url = reverse_lazy('loans:insurance_list')
    permission_required = 'add_insurance'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar seguro'
        context['back_url'] = self.success_url
        return context


class InsuranceUpdateView(UpdateViewMixin, UpdateView):
    model = Insurance
    template_name = 'insurance/form.html'
    form_class = InsuranceForm
    success_url = reverse_lazy('loans:insurance_list')
    permission_required = 'change_insurance'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar seguro'
        context['back_url'] = self.success_url
        return context


class InsuranceDeleteView(DeleteViewMixin, DeleteView):
    model = Insurance
    template_name = 'insurance/delete.html'
    success_url = reverse_lazy('loans:insurance_list')
    permission_required = 'delete_insurance'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar seguro'

        context['description'] = f"¿Desea Eliminar el seguro de: {self.object.employee}?"

        context['back_url'] = self.success_url
        return context
