from django.urls import reverse_lazy
from apps.loans.models import Entry
from apps.loans.forms.entry import EntryForm

from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.db.models import Q
from apps.security.mixins.mixins import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin, PermissionMixin


class EntryListView(PermissionMixin, ListViewMixin, ListView):
    model = Entry
    template_name = 'entry/list.html'
    context_object_name = 'entries'

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
        context['title'] = 'rubros'
        context['create_url'] = reverse_lazy('loans:entry_create')
        return context


class EntryCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = Entry
    template_name = 'entry/form.html'
    form_class = EntryForm
    success_url = reverse_lazy('loans:entry_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Ingresar nuevo rubro'
        context['grabar'] = 'Grabar rubro'
        context['back_url'] = self.success_url
        return context


class EntryUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = Entry
    template_name = 'entry/form.html'
    form_class = EntryForm
    success_url = reverse_lazy('loans:entry_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Actualizar el rubro'
        context['grabar'] = 'Actualizar rubro'
        context['back_url'] = self.success_url
        return context


class EntryDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = Entry
    template_name = 'entry/delete.html'
    success_url = reverse_lazy('loans:entry_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Eliminar el rubro'
        context['grabar'] = 'Eliminar rubro'
        context['description'] = f"¿Desea Eliminar la rubro: {self.object.name}?"
        context['back_url'] = self.success_url
        return context
