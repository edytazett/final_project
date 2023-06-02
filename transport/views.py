from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from transport.forms import ClientCreateForm, OrderCreateForm, PersonCreateForm, EmployeeCreateForm, TruckCreateForm, \
    TrailerCreateForm

from transport.models import Client, Order, Person, Employee, Truck, Trailer


class MainPageView(View):
    def get(self, request):
        return render(request, 'index2.html')


class DashboardView(View):
    def get(self, request):
        return render(request, 'dashboard2.html')


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientCreateForm
    template_name = 'form.html'


class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'form.html'
    exclude = ['creation_date']


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonCreateForm
    template_name = 'form.html'


class PersonUpdateView(UpdateView):
    model = Person
    template_name = 'form.html'
    fields = '__all__'


class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeCreateForm
    template_name = 'form.html'


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'form.html'
    fields = '__all__'


class TruckCreateView(CreateView):
    model = Truck
    form_class = TruckCreateForm
    template_name = 'form.html'


class TruckUpdateView(UpdateView):
    model = Truck
    template_name = 'form.html'
    fields = '__all__'


class TrailerCreateView(CreateView):
    model = Trailer
    form_class = TrailerCreateForm
    template_name = 'form.html'


class TrailerUpdateView(UpdateView):
    model = Trailer
    template_name = 'form.html'
    fields = '__all__'


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderCreateForm
    template_name = 'form.html'


class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'form.html'
    fields = '__all__'


class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'
    paginate_by = 100


class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'
    paginate_by = 100
