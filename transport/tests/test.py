from transport.models import Customer, Person, Employee, Trailer, Truck, Order
import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_customer_model(company1):
    assert len(Customer.objects.all()) == 1
    assert Customer.objects.get(name_short='Krzak') == company1


@pytest.mark.django_db
def test_person_model(person1):
    assert len(Person.objects.all()) == 1
    assert Person.objects.get(email='janina.o@krzak.pl') == person1


@pytest.mark.django_db
def test_employee_model(employee1):
    assert len(Employee.objects.all()) == 1
    assert Employee.objects.get(surname='Kowalski') == employee1


@pytest.mark.django_db
def test_trailer_model(trailer1):
    assert len(Trailer.objects.all()) == 1
    assert Trailer.objects.get(plate_number='WGM00000') == trailer1


@pytest.mark.django_db
def test_trailer_model(truck1):
    assert len(Truck.objects.all()) == 1
    assert Truck.objects.get(plate_number='WGM11111') == truck1


@pytest.mark.django_db
def test_order_model(order1):
    assert len(Order.objects.all()) == 1
    assert Order.objects.get(order_number='1999/T/2023/E') == order1


@pytest.mark.django_db
def test_main_page():
    client = Client()
    url = reverse('main_page')
    response = client.get(url)
    assert response.status_code == 200

    
@pytest.mark.django_db
def test_dashboard(client, user):
    client.force_login(user)
    url = reverse('dashboard')
    response = client.get(url)
    assert response.status_code == 200
    

@pytest.mark.django_db
def test_dashboard_not_login(client):
    url = reverse('dashboard')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_mycompanyview(client, user):
    client.force_login(user)
    url = reverse('my_company')
    response = client.get(url)
    assert response.status_code == 200
    
    
@pytest.mark.django_db
def test_mycompanyview_not_login(client):
    url = reverse('my_company')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_exportsview(client, user):
    client.force_login(user)
    url = reverse('exports')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_exportsview_not_login(client):
    url = reverse('my_company')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_importsview(client, user):
    client.force_login(user)
    url = reverse('imports')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_importsview_not_login(client):
    url = reverse('my_company')
    response = client.get(url)
    assert response.status_code == 302
    
    
@pytest.mark.django_db
def test_customerlistview(client, user):
    client.force_login(user)
    url = reverse('customer_list')
    response = client.get(url)
    assert response.status_code == 200
    
    
@pytest.mark.django_db
def test_customerlistview_not_login(client):
    url = reverse('customer_list')
    response = client.get(url)
    assert response.status_code == 302
    
    
@pytest.mark.django_db
def test_orderlistview(client, user):
    client.force_login(user)
    url = reverse('order_list')
    response = client.get(url)
    assert response.status_code == 200
    
 
@pytest.mark.django_db
def test_orderlistview_not_login(client):
    url = reverse('orderr_list')
    response = client.get(url)
    assert response.status_code == 302
    

@pytest.mark.django_db
def test_customercreateview_no_permission(client, user):
    client.force_login(user)
    url = reverse('customer_create')
    response = client.get(url)
    assert response.status_code == 403
    
    
@pytest.mark.django_db
def test_customercreateview(client, user_with_permission):
    client.force_login(user_with_permission)
    url = reverse('customer_create')
    response = client.get(url)
    assert response.status_code == 200
    
