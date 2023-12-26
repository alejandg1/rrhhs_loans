from django.urls import reverse_lazy
from apps.loans.models import Employee
from apps.loans.forms.employee import EmployeeForm

from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.db.models import Q
from apps.security.mixins.mixins import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin


class EmployeeListView(ListViewMixin, ListView):
    model = Employee
    template_name = 'employee/list.html'
    context_object_name = 'employees'
    paginate_by = 2
    query = None

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
        context['title'] = 'empleados'
        context['create_url'] = reverse_lazy('loans:employee_create')
        return context


class EmployeeCreateView(CreateViewMixin, CreateView):
    model = Employee
    template_name = 'employee/form.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('loans:employee_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Ingresar nuevo empleado'
        context['grabar'] = 'Grabar empleado'
        context['back_url'] = self.success_url
        return context


class EmployeeUpdateView(UpdateViewMixin, UpdateView):
    model = Employee
    template_name = 'employee/form.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('loans:employee_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Actualizar el empleado'
        context['grabar'] = 'Actualizar empleado'
        context['back_url'] = self.success_url
        return context


class EmployeeDeleteView(DeleteViewMixin, DeleteView):
    model = Employee
    template_name = 'employee/delete.html'
    success_url = reverse_lazy('loans:employee_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Eliminar el empleado'
        context['grabar'] = 'Eliminar empleado'
        context['description'] = f"¿Desea Eliminar la empleado: {self.object.name}?"
        context['back_url'] = self.success_url
        return context
