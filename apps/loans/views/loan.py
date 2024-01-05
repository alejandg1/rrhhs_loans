
from django.urls import reverse_lazy
from apps.loans.models import Loan
from apps.loans.forms.loan import LoanForm
from apps.security.mixins.mixins import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin, PermissionMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.db.models import Q


class LoanListView(ListViewMixin, ListView):
    model = Loan
    template_name = 'loan/list.html'
    context_object_name = 'loans'
    permission_required = 'view_loan'

    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get('q1')  # ver
        if q1 is not None:
            self.query.add(Q(name__icontains=q1), Q.AND)
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'seguros'
        context['create_url'] = reverse_lazy('loans:loan_create')
        context['permission_add'] = context['permissions'].get(
            'add_loan', '')
        return context


class LoanCreateView(CreateViewMixin, CreateView):
    model = Loan
    template_name = 'loan/form.html'
    form_class = LoanForm
    success_url = reverse_lazy('loans:loan_list')
    permission_required = 'add_loan'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar seguro'
        context['back_url'] = self.success_url
        return context


class LoanUpdateView(UpdateViewMixin, UpdateView):
    model = Loan
    template_name = 'loan/form.html'
    form_class = LoanForm
    success_url = reverse_lazy('loans:loan_list')
    permission_required = 'change_loan'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar seguro'
        context['back_url'] = self.success_url
        return context


class LoanDeleteView(DeleteViewMixin, DeleteView):
    model = Loan
    template_name = 'loan/delete.html'
    success_url = reverse_lazy('loans:loan_list')
    permission_required = 'delete_loan'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar seguro'
        context['description'] = f"¿Desea Eliminar el seguro: {self.object.id}?"
        context['back_url'] = self.success_url
        return context
