from django.urls import reverse_lazy
from apps.loans.models import Payment
from apps.loans.forms.payment import PaymentForm

from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.db.models import Q
from apps.security.mixins.mixins import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin, PermissionMixin


class PaymentListView(ListViewMixin, ListView):
    model = Payment
    template_name = 'payment/list.html'
    context_object_name = 'payments'
    permission_required = 'view_payment'

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
        context['title'] = 'pagos'
        context['create_url'] = reverse_lazy('loans:payment_create')
        context['permission_add'] = context['permissions'].get(
            'add_payment', '')
        return context


class PaymentCreateView(CreateViewMixin, CreateView):
    model = Payment
    template_name = 'payment/form.html'
    form_class = PaymentForm
    success_url = reverse_lazy('loans:payment_list')
    permission_required = 'add_payment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar pago'
        context['back_url'] = self.success_url
        return context


class PaymentUpdateView(UpdateViewMixin, UpdateView):
    model = Payment
    template_name = 'payment/form.html'
    form_class = PaymentForm
    success_url = reverse_lazy('loans:payment_list')
    permission_required = 'change_payment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar pago'
        context['back_url'] = self.success_url
        return context


class PaymentDeleteView(DeleteViewMixin, DeleteView):
    model = Payment
    template_name = 'payment/delete.html'
    success_url = reverse_lazy('loans:payment_list')
    permission_required = 'delete_payment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar pago'
        context['description'] = f"¿Desea Eliminar el pago: {self.object.code}?"
        context['back_url'] = self.success_url
        return context
