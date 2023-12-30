from django.urls import reverse_lazy
from apps.loans.models import Fee
from apps.loans.forms.fee import FeeForm

from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.db.models import Q
from apps.security.mixins.mixins import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin, PermissionMixin


class FeeListView(ListViewMixin, ListView):
    model = Fee
    template_name = 'fee/list.html'
    context_object_name = 'fees'
    permission_required = 'view_fee'

    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get('q1')  # ver
        if q1 is not None:
            self.query.add(Q(code__icontains=q1), Q.AND)
        # q2 = self.request.GET.get('q2') # ver
        # if q2 is not None:
        #     query.add(Q(estado__icontains=q2), Q.AND)
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'cuotas'
        context['create_url'] = reverse_lazy('loans:fee_create')
        context['permission_add'] = context['permissions'].get(
            'add_fee', '')
        return context


class FeeCreateView(CreateViewMixin, CreateView):
    model = Fee
    template_name = 'fee/form.html'
    form_class = FeeForm
    success_url = reverse_lazy('loans:fee_list')
    permission_required = 'add_fee'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar cuota'
        context['back_url'] = self.success_url
        return context


class FeeUpdateView(UpdateViewMixin, UpdateView):
    model = Fee
    template_name = 'fee/form.html'
    form_class = FeeForm
    success_url = reverse_lazy('loans:fee_list')
    permission_required = 'change_fee'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar cuota'
        context['back_url'] = self.success_url
        return context


class FeeDeleteView(DeleteViewMixin, DeleteView):
    model = Fee
    template_name = 'fee/delete.html'
    success_url = reverse_lazy('loans:fee_list')
    permission_required = 'delete_fee'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar cuota'
        context['description'] = f"¿Desea Eliminar la cuota: {self.object.code}?"
        context['back_url'] = self.success_url
        return context
