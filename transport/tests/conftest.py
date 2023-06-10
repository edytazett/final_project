from transport.models import Customer, Person, Employee, Trailer, Truck, Order
import pytest
from django.test import Client


@pytest.fixture
def company1():
    company1 = Customer.objects.create(name_full='Krzak sp.zo.o.',
                                       name_short='Krzak',
                                       address_street='ul. Konwaliowa 10',
                                       address_postcode='09-918',
                                       address_city='Korczyn',
                                       address_country='Polska',
                                       vat_number='8881119900',
                                       email='krzak@krzak.pl',
                                       phone_number='+48500000000',
                                       payment_term=45,
                                       exchange_rate=-1,
                                       payment_email='platnosci@krzak.pl',
                                       payment_phone_number='+48500000001',
                                       mailing_address_street='ul. Konwaliowa 11',
                                       mailing_address_postcode='09-918',
                                       mailing_address_city='Korczyn',
                                       mailing_address_country='Polska')
    return company1


@pytest.fixture
def person1(company1):
    person1 = Person.objects.create(name='Janina',
                                    surname='Odrzywołek',
                                    company=company1,
                                    phone_number='+48900900900',
                                    email='janina.o@krzak.pl',
                                    still_active=True)
    return person1


@pytest.fixture
def employee1():
    employee1 = Employee.objects.create(name='Janusz',
                                        surname='Kowalski',
                                        position='Driver',
                                        department='Transport',
                                        start_work_date='2023-03-03')
    return employee1


@pytest.fixture
def trailer1():
    trailer1 = Trailer.objects.create(plate_number='WGM00000',
                                      type='tautliner',
                                      height='275')
    return trailer1


@pytest.fixture
def truck1(employee1, trailer1):
    truck1 = Truck.objects.create(plate_number='WGM11111',
                                  driver=employee1,
                                  trailer=trailer1,
                                  capacity=24,
                                  year=2022)
    return truck1


@pytest.fixture
def order1(company1, person1, trailer1, truck1, employee1):
    order1 = Order.objects.create(creation_date='2023-06-05',
                                  order_number='1999/T/2023/E',
                                  order_type=0,
                                  pick_up_date='2023-06-12',
                                  pick_up_company='P&G',
                                  pick_up_street='ul. Spedycyjna 111',
                                  pick_up_city='Warszawa',
                                  pick_up_postcode='PL00-111',
                                  pick_up_country='PL',
                                  pick_up_reference='CFSTFD782023',
                                  pick_up_comments='załadunek z rampy',

                                  delivery_date='2023-06-14',
                                  delivery_company='Transport SRL',
                                  delivery_street='via Venezia 12',
                                  delivery_city='Milano',
                                  delivery_postcode='IT20010',
                                  delivery_country='IT',

                                  pallets_number=10,
                                  pallets_size='80x120',
                                  ldm=4.0,
                                  weight=3.5,
                                  price=1000,

                                  customer=company1,
                                  customer_contact_person=person1,
                                  payment_term=30,
                                  truck=truck1,
                                  trailer=trailer1)
    return order1


@pytest.fixture
def customer_list1(company1):
    customer_list1 = []
    customer_list1.append(company1)
    customer_list1.append(Customer.objects.create(name_full='Drzewo sp.zo.o.',
                                                  name_short='Drzewo',
                                                  address_street='ul. Bukowa 10',
                                                  address_postcode='09-910',
                                                  address_city='Dąbrowo',
                                                  address_country='Polska',
                                                  vat_number='8881119999',
                                                  email='drzewo@drzewo.pl',
                                                  phone_number='+48600000000',
                                                  payment_term=45,
                                                  exchange_rate=-1,
                                                  payment_email='platnosci@drzewo.pl',
                                                  payment_phone_number='+48600000001',
                                                  mailing_address_street='ul. Sosnowa 11',
                                                  mailing_address_postcode='09-100',
                                                  mailing_address_city='Brzózka',
                                                  mailing_address_country='Polska'))
    customer_list1.append(Customer.objects.create(name_full='Kwiatek i syn sp.zo.o.',
                                                  name_short='Kwiatek',
                                                  address_street='ul. Różana 10',
                                                  address_postcode='00-910',
                                                  address_city='Stokrotka',
                                                  address_country='Polska',
                                                  vat_number='2221119999',
                                                  email='kwiatek@kwiatekisyn.pl',
                                                  phone_number='+48900000000',
                                                  payment_term=45,
                                                  exchange_rate=-1,
                                                  payment_email='platnosci@kwiatekisyn.pl',
                                                  payment_phone_number='+48900000001',
                                                  mailing_address_street='ul. Różana 11',
                                                  mailing_address_postcode='00-910',
                                                  mailing_address_city='Stokrotka',
                                                  mailing_address_country='Polska'))
    return list


@pytest.fixture
def client():
    client = Client()
    return client


@pytest.fixture
def user():
    u = User.objects.create(username='uzytkownik')
    return u
