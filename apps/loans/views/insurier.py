
from django.urls import reverse_lazy
from apps.loans.models import Insurier
from apps.loans.forms.insurier import InsurierForm
from apps.security.mixins.mixins import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin, PermissionMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.db.models import Q
from apps.security.mixins.mixins import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin


class InsurierListView(PermissionMixin, ListViewMixin, ListView):
    model = Insurier
    template_name = 'insurier/list.html'
    context_object_name = 'insurier'
    permission_required = 'view_insurier'
    paginate_by = 2
    query = None

    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get('q1')  # ver
        if q1 is not None:
            self.query.add(Q(name__icontains=q1), Q.AND)
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Aseguradoras'
        context['create_url'] = reverse_lazy('loans:insurier_create')
        context['permission_add'] = context['permissions'].get(
            'add_insurier', '')
        return context


class InsurierCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = Insurier
    template_name = 'insurier/form.html'
    form_class = InsurierForm
    success_url = reverse_lazy('loans:insurier_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Ingresar nueva aseguradora'
        context['grabar'] = 'Grabar aseguradora'
        context['back_url'] = self.success_url
        return context


class InsurierUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = Insurier
    template_name = 'insurier/form.html'
    form_class = InsurierForm
    success_url = reverse_lazy('loans:insurier_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Actualizar la aseguradora'
        context['grabar'] = 'Actualizar aseguradora'
        context['back_url'] = self.success_url
        return context


class InsurierDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = Insurier
    template_name = 'insurier/delete.html'
    success_url = reverse_lazy('loans:insurier_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Eliminar la aseguradora'
        context['grabar'] = 'Eliminar aseguradora'
        context['description'] = f"¿Desea Eliminar la aseguradora: {self.object.name}?"
        context['back_url'] = self.success_url
        return context
