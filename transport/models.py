from django.db import models
from django.urls import reverse


class Customer(models.Model):
    """
    Model representing Customer of the company(user) with it's registration data, payment information and contact details.
    """
    DAY_OF_SELL = -1
    DAY_BEFORE_ORDER = 0
    DAY_OF_PICKUP = 1
    DAY_BEFORE_PICKUP = 2
    EXCHANGE_RATE_CHOICES = (
        (DAY_OF_SELL, 'poprzedzającego sprzedaż'),
        (DAY_BEFORE_ORDER, 'poprzedzającego wystawienie zlecenia'),
        (DAY_OF_PICKUP, 'załadunku'),
        (DAY_BEFORE_PICKUP, 'poprzedzającego dzień załadunku')
    )
    name_full = models.CharField(max_length=128, verbose_name='Nazwa firmy')
    name_short = models.CharField(max_length=128, verbose_name='Nazwa skrócona', unique=True)
    address_street = models.CharField(max_length=128, verbose_name='Ulica i numer')
    address_postcode = models.CharField(max_length=8, verbose_name='Kod pocztowy')
    address_city = models.CharField(max_length=128, verbose_name='Miejscowość')
    address_country = models.CharField(max_length=128, verbose_name='Kraj')
    vat_number = models.CharField(max_length=60, unique=True, verbose_name='Numer NIP')
    email = models.CharField(max_length=128, verbose_name='e-mail')
    phone_number = models.CharField(max_length=30, verbose_name='Numer telefonu')

    payment_term = models.IntegerField(verbose_name='Termin płatności')
    exchange_rate = models.IntegerField(choices=EXCHANGE_RATE_CHOICES, default=-1, verbose_name='Kurs waluty z dnia')
    payment_email = models.CharField(max_length=128, verbose_name='E-mail do płatności')
    payment_phone_number = models.CharField(max_length=128, null=True, verbose_name='Numer telefonu do płatności')

    mailing_address_street = models.CharField(max_length=128, null=True, verbose_name='Ulica i numer (korespondencja)')
    mailing_address_postcode = models.CharField(max_length=8, null=True, verbose_name='Kod pocztowy (korespondencja)')
    mailing_address_city = models.CharField(max_length=128, null=True, verbose_name='Miejsowość (korespondencja)')
    mailing_address_country = models.CharField(max_length=128, null=True, verbose_name='Kraj (korespondencja)')
    creation_date = models.DateField(auto_now_add=True, blank=True)

    def get_absolute_url(self):
        return reverse('customer_update', kwargs={'pk': self.id})


class Person(models.Model):
    """
    Model representing people other than our company employees (users of the application) e.g. customer employees.
    """
    name = models.CharField(max_length=128, verbose_name='Imię')
    surname = models.CharField(max_length=128, verbose_name='Nazwisko')
    company = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Firma')
    phone_number = models.CharField(max_length=128, verbose_name='Numer telefonu')
    email = models.CharField(max_length=128, verbose_name='e-mail')
    still_active = models.BooleanField(default=True, verbose_name='Pracownik aktywny')


class Employee(models.Model):
    POSITIONS = (
        ('Driver', 'Driver'),
        ('Freight Forwarder', 'Freight Forwarder'),
        ('Senior Freight Forwarder', 'Senior Freight Forwarder'),
        ('Owner', 'Owner'),
        ('Office', 'Office')
    )
    DEPARTMENTS = (
        ('Spedycja', 'Spedycja'),
        ('Księgowość', 'Księgowość'),
        ('Zarząd', 'Zarząd'),
        ('Transport', 'Transport'),
    )
    name = models.CharField(max_length=128, verbose_name='Imię')
    surname = models.CharField(max_length=128, verbose_name='Nazwisko')
    position = models.CharField(choices=POSITIONS, verbose_name='Stanowisko', max_length=128)
    department = models.CharField(choices=DEPARTMENTS, verbose_name='Dział', max_length=128)
    start_work_date = models.DateField(verbose_name='Zatrudniony od')
    end_work_date = models.DateField(null=True, verbose_name='Zakończenie pracy')


class Trailer(models.Model):
    plate_number = models.CharField(max_length=8, verbose_name='Numer rejestracyjny')
    type = models.CharField(max_length=128, verbose_name='Typ', default='brak danych') #dodac choices
    height = models.IntegerField(verbose_name='Wysokość (cm)', default='brak danych')

    def get_absolute_url(self):
        return reverse('trailer_update', kwargs={'pk': self.id})


class Truck(models.Model):
    plate_number = models.CharField(max_length=8, verbose_name='Numer rejestracyjny')
    driver = models.OneToOneField(Employee, on_delete=models.SET_NULL, null=True, verbose_name='Kierowca')
    trailer = models.OneToOneField(Trailer, on_delete=models.SET_NULL, null=True, verbose_name='Naczepa')
    type = models.CharField(max_length=128, verbose_name='Typ', default='brak danych')
    capacity = models.IntegerField(verbose_name='Ładowność', default=0)
    year = models.IntegerField(verbose_name='Rok produkcji', default=0)

    def get_absolute_url(self):
        return reverse('truck_update', kwargs={'pk': self.id})


class Order(models.Model):
    """ Model representing the transport order. """
    EXPORT = 0
    IMPORT = 1
    KRAJ = 2
    INNE = 3
    ORDER_TYPES = (
        (EXPORT, 'EXPORT'),
        (IMPORT, 'IMPORT'),
        (KRAJ, 'PRZEWÓZ KRAJOWY'),
        (INNE, 'INNE')
    )

    PALLETS = (
        ('80x120', '80x120'),
        ('100x120', '100x120'),
        ('120X120', '120X120'),
        ('60x80', '60x80'),
        ('inne', 'inne'), #jak tu zrobic mozliwosc wpisania recznego?

    )
    creation_date = models.DateField(verbose_name='Zlecenie z dnia')
    order_number = models.CharField(max_length=128, verbose_name='Numer zlecenia', unique=True)
    order_type = models.IntegerField(choices=ORDER_TYPES, verbose_name='Typ zlecenia')
    pick_up_date = models.DateField(verbose_name='Dzień załadunku')
    pick_up_date_fix = models.IntegerField(null=True, verbose_name='Godzina awizacji')
    pick_up_company = models.CharField(max_length=128, verbose_name='Nazwa firmy (załadunek)') #czy da sie tu wstawic wyszukiwarke z google np z rzeczywistym adresem?
    pick_up_street = models.CharField(max_length=128, verbose_name='Ulica i numer (załadunek)')
    pick_up_city = models.CharField(max_length=128, verbose_name='Miejscowość (załadunek)')
    pick_up_postcode = models.CharField(max_length=8, verbose_name='Kod pocztowy (załadunek)')
    pick_up_country = models.CharField(max_length=128, verbose_name='Kraj (załadunek)')
    pick_up_reference = models.CharField(max_length=128, null=True, verbose_name='Numer referencyjny (załadunek)')
    pick_up_comments = models.TextField(null=True, verbose_name='Komentarze (załadunek)')

    delivery_date = models.DateField(verbose_name='Data rozładunku')
    delivery_date_fix = models.IntegerField(null=True, verbose_name='Godzina awizacji')
    delivery_company = models.CharField(max_length=128, verbose_name='Nazwa firmy (rozładunek)')  # czy da sie tu wstawic wyszukiwarke z google np z rzeczywistym adresem?
    delivery_street = models.CharField(max_length=128, verbose_name='Ulica i numer (rozładunek)')
    delivery_city = models.CharField(max_length=128, verbose_name='Miejscowość (rozładunek)')
    delivery_postcode = models.CharField(max_length=8, verbose_name='Kod pocztowy (rozładunek)')
    delivery_country = models.CharField(max_length=128, verbose_name='Kraj (rozładunek)')
    delivery_reference = models.CharField(max_length=128, null=True, verbose_name='Numer referencyjny (rozładunek)')
    delivery_comments = models.TextField(null=True, verbose_name='Komentarze (rozładunek)')

    pallets_number = models.IntegerField(verbose_name='Liczba palet')
    pallets_size = models.CharField(choices=PALLETS, max_length=128, verbose_name='Rozmiar palet')
    ldm = models.FloatField(verbose_name='LDM')
    cubic_meters = models.FloatField(null=True, verbose_name='Metry sześcienne')
    weight = models.FloatField(verbose_name='Waga (t)')
    price = models.IntegerField(verbose_name='Stawka (eur)')

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, verbose_name='Kontrahent')
    customer_order_number = models.CharField(max_length=128, default='-', verbose_name='Numer zlecenia Komtrahenta')
    customer_contact_person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, verbose_name='Osoba kontaktowa')
    payment_term = models.IntegerField(verbose_name='Termin płatności') #pobrac i wyswietlic dane z modelu Customer ale mozliwe do edycji i oddzielne
    truck = models.ForeignKey(Truck, on_delete=models.PROTECT, verbose_name='Ciągnik')
    trailer = models.ForeignKey(Trailer, on_delete=models.PROTECT, verbose_name='Naczepa')

    def get_absolute_url(self):
        return reverse('order_update', kwargs={'pk': self.id})
