from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from transport.forms import CustomerCreateForm, OrderCreateForm, PersonCreateForm, EmployeeCreateForm, TruckCreateForm, \
    TrailerCreateForm

from transport.models import Customer, Order, Person, Employee, Truck, Trailer


class MainPageView(View):
    """Main page view before logging in."""
    def get(self, request):
        return render(request, 'index2.html')


class DashboardView(LoginRequiredMixin, View):
    """First view after logging in to the application."""
    def get(self, request):
        return render(request, 'dashboard2.html')


class MyCompanyView(LoginRequiredMixin, View):
    """
    Company details view with an option to add, update or delete information regarding trucks and employees.
    """
    def get(self, request):
        employees = Employee.objects.all()
        trucks = Truck.objects.all()

        return render(request, 'company.html', {'employees': employees,
                                                'trucks': trucks})


class ExportsView(LoginRequiredMixin, View):
    """View with export orders divided into free and assigned to specific trucks."""
    def get(self, request):
        exports = Order.objects.filter(order_type=0)
        return render(request, 'exports.html', {'orders': exports})


class ImportsView(LoginRequiredMixin, View):
    """View with import orders divided into free and assigned to specific trucks"""
    def get(self, request):
        imports = Order.objects.filter(order_type=1)
        return render(request, 'imports.html', {'orders': imports})


class CustomerCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ['add_customer']
    model = Customer
    form_class = CustomerCreateForm
    template_name = 'form.html'
    success_url = reverse_lazy('customer_list')


class CustomerUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['change_customer']
    model = Customer
    template_name = 'form.html'
    exclude = ['creation_date']


class PersonCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ['add_person']
    model = Person
    form_class = PersonCreateForm
    template_name = 'form.html'
    success_url = reverse_lazy('customer_list')


class PersonUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['change_person']
    model = Person
    template_name = 'form.html'
    fields = '__all__'
    success_url = reverse_lazy('customer_list')


class EmployeeCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ['add_employee']
    model = Employee
    form_class = EmployeeCreateForm
    template_name = 'form.html'
    success_url = reverse_lazy('my_company')


class EmployeeUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['change_employee']
    model = Employee
    template_name = 'form.html'
    fields = '__all__'
    success_url = reverse_lazy('my_company')


class TruckCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ['add_truck']
    model = Truck
    form_class = TruckCreateForm
    template_name = 'form.html'
    success_url = reverse_lazy('my_company')


class TruckUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['change_truck']
    model = Truck
    template_name = 'form.html'
    fields = '__all__'
    success_url = reverse_lazy('my_company')


class TrailerCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ['add_trailer']
    model = Trailer
    form_class = TrailerCreateForm
    template_name = 'form.html'


class TrailerUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['change_trailer']
    model = Trailer
    template_name = 'form.html'
    fields = '__all__'


class OrderCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ['add_order']
    model = Order
    form_class = OrderCreateForm
    template_name = 'form.html'
    success_url = reverse_lazy('order_list')


class OrderUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['change_order']
    model = Order
    template_name = 'form.html'
    fields = '__all__'


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order_list.html'
    paginate_by = 100


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'client_list.html'
    paginate_by = 100
