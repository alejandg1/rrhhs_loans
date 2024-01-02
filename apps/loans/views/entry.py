from django.urls import reverse_lazy
from apps.loans.models import Entry
from apps.loans.forms.entry import EntryForm

from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.db.models import Q
from apps.security.mixins.mixins import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin, PermissionMixin


class EntryListView(ListViewMixin, ListView):
    model = Entry
    template_name = 'entry/list.html'
    context_object_name = 'entries'
    permission_required = 'view_entry'

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
        context['title'] = 'rubros'
        context['create_url'] = reverse_lazy('loans:entry_create')
        context['permission_add'] = context['permissions'].get(
            'add_entry', '')
        return context


class EntryCreateView(CreateViewMixin, CreateView):
    model = Entry
    template_name = 'entry/form.html'
    form_class = EntryForm
    success_url = reverse_lazy('loans:entry_list')
    permission_required = 'add_entry'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar rubro'
        context['back_url'] = self.success_url
        return context


class EntryUpdateView(UpdateViewMixin, UpdateView):
    model = Entry
    template_name = 'entry/form.html'
    form_class = EntryForm
    success_url = reverse_lazy('loans:entry_list')
    permission_required = 'change_entry'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar rubro'
        context['back_url'] = self.success_url
        return context


class EntryDeleteView(DeleteViewMixin, DeleteView):
    model = Entry
    template_name = 'entry/delete.html'
    success_url = reverse_lazy('loans:entry_list')
    permission_required = 'delete_entry'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar rubro'
        context['description'] = f"¿Desea Eliminar el rubro: {self.object.employee}?"
        context['back_url'] = self.success_url
        return context
