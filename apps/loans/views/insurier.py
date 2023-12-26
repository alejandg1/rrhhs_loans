
from django.urls import reverse_lazy
from apps.loans.models import Insurier
from apps.loans.forms.insurier import InsurierForm
from apps.security.mixins.mixins import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin, PermissionMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.db.models import Q


class InsurierListView(ListViewMixin, ListView):
    model = Insurier
    template_name = 'insurier/list.html'
    context_object_name = 'insuriers'
    permission_required = 'view_insurier'

    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get('q1')  # ver
        if q1 is not None:
            self.query.add(Q(name__icontains=q1), Q.AND)
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('loans:insurier_create')
        context['permission_add'] = context['permissions'].get(
            'add_insurier', '')
        return context


class InsurierCreateView(CreateViewMixin, CreateView):
    model = Insurier
    template_name = 'insurier/form.html'
    form_class = InsurierForm
    success_url = reverse_lazy('loans:insurier_list')
    permission_required = 'add_insurier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar aseguradora'
        context['back_url'] = self.success_url
        return context


class InsurierUpdateView(UpdateViewMixin, UpdateView):
    model = Insurier
    template_name = 'insurier/form.html'
    form_class = InsurierForm
    success_url = reverse_lazy('loans:insurier_list')
    permission_required = 'change_insurier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar aseguradora'
        context['back_url'] = self.success_url
        return context


class InsurierDeleteView(DeleteViewMixin, DeleteView):
    model = Insurier
    template_name = 'insurier/delete.html'
    success_url = reverse_lazy('loans:insurier_list')
    permission_required = 'delete_insurier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar aseguradora'
        context['description'] = f"¿Desea Eliminar la aseguradora: {self.object.name}?"
        context['back_url'] = self.success_url
        return context
