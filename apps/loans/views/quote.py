from django.urls import reverse_lazy
from apps.loans.models import Quote
from apps.loans.forms.quote import QuoteForm

from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.db.models import Q
from apps.security.mixins.mixins import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin, PermissionMixin


class QuoteListView(ListViewMixin, ListView):
    model = Quote
    template_name = 'quote/list.html'
    context_object_name = 'quotes'
    permission_required = 'view_quote'

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
        context['create_url'] = reverse_lazy('loans:quote_create')
        context['permission_add'] = context['permissions'].get(
            'add_quote', '')
        return context


class QuoteCreateView(CreateViewMixin, CreateView):
    model = Quote
    template_name = 'quote/form.html'
    form_class = QuoteForm
    success_url = reverse_lazy('loans:quote_list')
    permission_required = 'add_quote'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar cuota'
        context['back_url'] = self.success_url
        return context


class QuoteUpdateView(UpdateViewMixin, UpdateView):
    model = Quote
    template_name = 'quote/form.html'
    form_class = QuoteForm
    success_url = reverse_lazy('loans:quote_list')
    permission_required = 'change_quote'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar cuota'
        context['back_url'] = self.success_url
        return context


class QuoteDeleteView(DeleteViewMixin, DeleteView):
    model = Quote
    template_name = 'quote/delete.html'
    success_url = reverse_lazy('loans:quote_list')
    permission_required = 'delete_quote'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar cuota'
        context['description'] = f"¿Desea Eliminar la cuota: {self.object.code}?"
        context['back_url'] = self.success_url
        return context
