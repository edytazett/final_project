# Generated by Django 4.2.1 on 2023-06-03 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_full', models.CharField(max_length=128, verbose_name='Nazwa firmy')),
                ('name_short', models.CharField(max_length=128, unique=True, verbose_name='Nazwa skrócona')),
                ('address_street', models.CharField(max_length=128, verbose_name='Ulica i numer')),
                ('address_postcode', models.CharField(max_length=6, verbose_name='Kod pocztowy')),
                ('address_city', models.CharField(max_length=128, verbose_name='Miejscowość')),
                ('address_country', models.CharField(max_length=128, verbose_name='Kraj')),
                ('vat_number', models.IntegerField(unique=True, verbose_name='Numer NIP')),
                ('email', models.CharField(max_length=128, verbose_name='e-mail')),
                ('phone_number', models.CharField(max_length=30, verbose_name='Numer telefonu')),
                ('payment_term', models.IntegerField(verbose_name='Termin płatności')),
                ('exchange_rate', models.IntegerField(choices=[(-1, 'poprzedzającego sprzedaż'), (0, 'poprzedzającego wystawienie zlecenia'), (1, 'załadunku'), (2, 'poprzedzającego dzień załadunku')], default=-1, verbose_name='Kurs waluty z dnia')),
                ('payment_email', models.CharField(max_length=128, verbose_name='E-mail do płatności')),
                ('payment_phone_number', models.CharField(max_length=128, null=True, verbose_name='Numer telefonu do płatności')),
                ('mailing_address_street', models.CharField(max_length=128, null=True, verbose_name='Ulica i numer (korespondencja)')),
                ('mailing_address_postcode', models.CharField(max_length=5, null=True, verbose_name='Kod pocztowy (korespondencja)')),
                ('mailing_address_city', models.CharField(max_length=128, null=True, verbose_name='Miejsowość (korespondencja)')),
                ('mailing_address_country', models.CharField(max_length=128, null=True, verbose_name='Kraj (korespondencja)')),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Imię')),
                ('surname', models.CharField(max_length=128, verbose_name='Nazwisko')),
                ('position', models.IntegerField(choices=[(0, 'Driver'), (1, 'Freight Forwarder'), (2, 'Senior Freight Forwarder'), (3, 'Owner'), (4, 'Office')], verbose_name='Stanowisko')),
                ('department', models.CharField(choices=[('Spedycja', 'Spedycja'), ('Księgowość', 'Księgowość'), ('Zarząd', 'Zarząd')], max_length=128, null=True, verbose_name='Dział')),
                ('start_work_date', models.DateField(verbose_name='Zatrudniony od')),
                ('end_work_date', models.DateField(null=True, verbose_name='Zakończenie pracy')),
            ],
        ),
        migrations.CreateModel(
            name='Trailer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate_number', models.CharField(max_length=8, verbose_name='Numer rejestracyjny')),
                ('type', models.CharField(default='brak danych', max_length=128, verbose_name='Typ')),
                ('height', models.IntegerField(default='brak danych', verbose_name='Wysokość (cm)')),
            ],
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate_number', models.CharField(max_length=8, verbose_name='Numer rejestracyjny')),
                ('type', models.CharField(default='brak danych', max_length=128, verbose_name='Typ')),
                ('capacity', models.IntegerField(default=0, verbose_name='Ładowność')),
                ('year', models.IntegerField(default=0, verbose_name='Rok produkcji')),
                ('driver', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='transport.employee', verbose_name='Kierowca')),
                ('trailer', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='transport.trailer', verbose_name='Naczepa')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Imię')),
                ('surname', models.CharField(max_length=128, verbose_name='Nazwisko')),
                ('phone_number', models.CharField(max_length=128, verbose_name='Numer telefonu')),
                ('email', models.CharField(max_length=128, verbose_name='e-mail')),
                ('still_active', models.BooleanField(default=True, verbose_name='Pracownik aktywny')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport.client', verbose_name='Firma')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(verbose_name='Zlecenie z dnia')),
                ('order_number', models.CharField(max_length=128, unique=True, verbose_name='Numer zlecenia')),
                ('order_type', models.IntegerField(choices=[(0, 'EXPORT'), (1, 'IMPORT'), (2, 'PRZEWÓZ KRAJOWY'), (3, 'INNE')], verbose_name='Typ zlecenia')),
                ('pick_up_date', models.DateField(verbose_name='Dzień załadunku')),
                ('pick_up_date_fix', models.IntegerField(null=True, verbose_name='Godzina awizacji')),
                ('pick_up_company', models.CharField(max_length=128, verbose_name='Nazwa firmy (załadunek)')),
                ('pick_up_street', models.CharField(max_length=128, verbose_name='Ulica i numer (załadunek)')),
                ('pick_up_city', models.CharField(max_length=128, verbose_name='Miejscowość (załadunek)')),
                ('pick_up_postcode', models.CharField(max_length=8, verbose_name='Kod pocztowy (załadunek)')),
                ('pick_up_country', models.CharField(max_length=128, verbose_name='Kraj (załadunek)')),
                ('pick_up_reference', models.CharField(max_length=128, null=True, verbose_name='Numer referencyjny (załadunek)')),
                ('pick_up_comments', models.TextField(null=True, verbose_name='Komentarze (załadunek)')),
                ('delivery_date', models.DateField(verbose_name='Data rozładunku')),
                ('delivery_date_fix', models.IntegerField(null=True, verbose_name='Godzina awizacji')),
                ('delivery_company', models.CharField(max_length=128, verbose_name='Nazwa firmy (rozładunek)')),
                ('delivery_street', models.CharField(max_length=128, verbose_name='Ulica i numer (rozładunek)')),
                ('delivery_city', models.CharField(max_length=128, verbose_name='Miejscowość (rozładunek)')),
                ('delivery_postcode', models.CharField(max_length=8, verbose_name='Kod pocztowy (rozładunek)')),
                ('delivery_country', models.CharField(max_length=128, verbose_name='Kraj (rozładunek)')),
                ('delivery_reference', models.CharField(max_length=128, null=True, verbose_name='Numer referencyjny (rozładunek)')),
                ('delivery_comments', models.TextField(null=True, verbose_name='Komentarze (rozładunek)')),
                ('pallets_number', models.IntegerField(verbose_name='Liczba palet')),
                ('pallets_size', models.CharField(choices=[('80x120', '80x120'), ('100x120', '100x120'), ('120X120', '120X120'), ('60x80', '60x80'), ('inne', 'inne')], max_length=128, verbose_name='Rozmiar palet')),
                ('ldm', models.FloatField(verbose_name='LDM')),
                ('cubic_meters', models.FloatField(null=True, verbose_name='Metry sześcienne')),
                ('weight', models.FloatField(verbose_name='Waga (t)')),
                ('price', models.IntegerField(verbose_name='Stawka (eur)')),
                ('client_order_number', models.CharField(max_length=128, verbose_name='Numer zlecenia Komtrahenta')),
                ('payment_term', models.IntegerField(verbose_name='Termin płatności')),
                ('truck', models.CharField(max_length=128)),
                ('trailer', models.CharField(max_length=128)),
                ('client_contact_person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='transport.person', verbose_name='Osoba kontaktowa')),
                ('client_vat_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='transport.client', verbose_name='NIP Kontrahenta')),
            ],
        ),
    ]
