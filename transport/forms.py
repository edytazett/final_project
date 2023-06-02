from django.forms import Form, ModelForm
from transport.models import Client, Person, Employee, Truck, Trailer, Order


class ClientCreateForm(ModelForm):
    class Meta:
        model = Client
        exclude = ['creation_date']


class PersonCreateForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


class EmployeeCreateForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


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
        