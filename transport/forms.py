from django.forms import Form, ModelForm
from transport.models import Customer, Person, Employee, Truck, Trailer, Order


class CustomerCreateForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ['creation_date']


class PersonCreateForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


class EmployeeCreateForm(ModelForm):
    class Meta:
        model = Employee
        exclude = ['end_work_date']


class TruckCreateForm(ModelForm):
    class Meta:
        model = Truck
        fields = '__all__'


class TrailerCreateForm(ModelForm):
    class Meta:
        model = Trailer
        fields = '__all__'


class OrderCreateForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        