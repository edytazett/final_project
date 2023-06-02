# Generated by Django 4.2.1 on 2023-05-28 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trailer',
            name='truck',
        ),
        migrations.AddField(
            model_name='order',
            name='trailer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='transport.trailer', verbose_name='Naczepa'),
        ),
        migrations.AddField(
            model_name='truck',
            name='trailer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='transport.trailer', verbose_name='Naczepa'),
        ),
        migrations.AlterField(
            model_name='client',
            name='address_city',
            field=models.CharField(max_length=128, verbose_name='Miejscowość'),
        ),
        migrations.AlterField(
            model_name='client',
            name='address_country',
            field=models.CharField(max_length=128, verbose_name='Kraj'),
        ),
        migrations.AlterField(
            model_name='client',
            name='address_postcode',
            field=models.CharField(max_length=5, verbose_name='Kod pocztowy'),
        ),
        migrations.AlterField(
            model_name='client',
            name='address_street',
            field=models.CharField(max_length=128, verbose_name='Ulica i numer'),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.CharField(max_length=128, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='client',
            name='exchange_rate',
            field=models.IntegerField(choices=[(-1, 'poprzedzającego sprzedaż'), (0, 'poprzedzającego wystawienie zlecenia'), (1, 'załadunku'), (2, 'poprzedzającego dzień załadunku')], default=-1, verbose_name='Kurs waluty z dnia'),
        ),
        migrations.AlterField(
            model_name='client',
            name='mailing_address_city',
            field=models.CharField(max_length=128, null=True, verbose_name='Miejsowość (korespondencja)'),
        ),
        migrations.AlterField(
            model_name='client',
            name='mailing_address_country',
            field=models.CharField(max_length=128, null=True, verbose_name='Kraj (korespondencja)'),
        ),
        migrations.AlterField(
            model_name='client',
            name='mailing_address_postcode',
            field=models.CharField(max_length=5, null=True, verbose_name='Kod pocztowy (korespondencja)'),
        ),
        migrations.AlterField(
            model_name='client',
            name='mailing_address_street',
            field=models.CharField(max_length=128, null=True, verbose_name='Ulica i numer (korespondencja)'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name_full',
            field=models.CharField(max_length=128, verbose_name='Nazwa firmy'),
        ),
        migrations.AlterField(
            model_name='client',
            name='payment_email',
            field=models.CharField(max_length=128, verbose_name='E-mail do płatności'),
        ),
        migrations.AlterField(
            model_name='client',
            name='payment_phone_number',
            field=models.CharField(max_length=128, null=True, verbose_name='Numer telefonu do płatności'),
        ),
        migrations.AlterField(
            model_name='client',
            name='payment_term',
            field=models.IntegerField(verbose_name='Termin płatności'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(max_length=30, verbose_name='Numer telefonu'),
        ),
        migrations.AlterField(
            model_name='client',
            name='vat_number',
            field=models.IntegerField(verbose_name='Numer NIP'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='end_work_date',
            field=models.DateField(null=True, verbose_name='Zakończenie pracy'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Imię'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.IntegerField(choices=[(0, 'Driver'), (1, 'Freight Forwarder'), (2, 'Senior Freight Forwarder'), (3, 'Owner'), (4, 'Office')], verbose_name='Stanowisko'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='start_work_date',
            field=models.DateField(verbose_name='Zatrudniony od'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='surname',
            field=models.CharField(max_length=128, verbose_name='Nazwisko'),
        ),
        migrations.AlterField(
            model_name='order',
            name='client_contact_person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='transport.person', verbose_name='Osoba kontaktowa'),
        ),
        migrations.AlterField(
            model_name='order',
            name='client_order_number',
            field=models.CharField(max_length=128, verbose_name='Numer zlecenia Komtrahenta'),
        ),
        migrations.AlterField(
            model_name='order',
            name='client_vat_number',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='transport.client', verbose_name='NIP Kontrahenta'),
        ),
        migrations.AlterField(
            model_name='order',
            name='creation_date',
            field=models.DateField(verbose_name='Zlecenie z dnia'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cubic_meters',
            field=models.FloatField(null=True, verbose_name='Metry sześcienne'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_city',
            field=models.CharField(max_length=128, verbose_name='Miejscowość (rozładunek)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_comments',
            field=models.TextField(null=True, verbose_name='Komentarze (rozładunek)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_company',
            field=models.CharField(max_length=128, verbose_name='Nazwa firmy (rozładunek)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_country',
            field=models.CharField(max_length=128, verbose_name='Kraj (rozładunek)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(verbose_name='Data rozładunku'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_date_fix',
            field=models.IntegerField(null=True, verbose_name='Godzina awizacji'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_postcode',
            field=models.CharField(max_length=5, verbose_name='Kod pocztowy (rozładunek)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_reference',
            field=models.CharField(max_length=128, null=True, verbose_name='Numer referencyjny (rozładunek)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_street',
            field=models.CharField(max_length=128, verbose_name='Ulica i numer (rozładunek)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='ldm',
            field=models.FloatField(verbose_name='LDM'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(max_length=128, verbose_name='Numer zlecenia'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_type',
            field=models.IntegerField(choices=[(0, 'EXPORT'), (1, 'IMPORT'), (2, 'PRZEWÓZ KRAJOWY'), (3, 'INNE')], verbose_name='Typ zlecenia'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pallets_number',
            field=models.IntegerField(verbose_name='Liczba palet'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pallets_size',
            field=models.CharField(choices=[('80x120', '80x120'), ('100x120', '100x120'), ('120X120', '120X120'), ('60x80', '60x80'), ('inne', 'inne')], verbose_name='Rozmiar palet'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_term',
            field=models.IntegerField(verbose_name='Termin płatności'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pick_up_city',
            field=models.CharField(max_length=128, verbose_name='Miejscowość (załadunek)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pick_up_comments',
            field=models.TextField(null=True, verbose_name='Komentarze (załadunek)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pick_up_company',
            field=models.CharField(max_length=128, verbose_name='Nazwa firmy (załadunek)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pick_up_country',
            field=models.CharField(max_length=128, verbose_name='Kraj (załadunek)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pick_up_date',
            field=models.DateField(verbose_name='Dzień załadunku'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pick_up_date_fix',
            field=models.IntegerField(null=True, verbose_name='Godzina awizacji'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pick_up_postcode',
            field=models.CharField(max_length=5, verbose_name='Kod pocztowy (załadunek)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pick_up_reference',
            field=models.CharField(max_length=128, null=True, verbose_name='Numer referencyjny (załadunek)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pick_up_street',
            field=models.CharField(max_length=128, verbose_name='Ulica i numer (załadunek)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='truck',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='transport.truck', verbose_name='Ciągnik'),
        ),
        migrations.AlterField(
            model_name='order',
            name='weight',
            field=models.FloatField(verbose_name='Waga (t)'),
        ),
        migrations.AlterField(
            model_name='person',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport.client', verbose_name='Firma'),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.CharField(max_length=128, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Imię'),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=models.CharField(max_length=128, verbose_name='Numer telefonu'),
        ),
        migrations.AlterField(
            model_name='person',
            name='still_active',
            field=models.BooleanField(default=True, verbose_name='Pracownik aktywny'),
        ),
        migrations.AlterField(
            model_name='person',
            name='surname',
            field=models.CharField(max_length=128, verbose_name='Nazwisko'),
        ),
        migrations.AlterField(
            model_name='trailer',
            name='plate_number',
            field=models.CharField(max_length=8, verbose_name='Numer rejestracyjny'),
        ),
        migrations.AlterField(
            model_name='truck',
            name='driver',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='transport.employee', verbose_name='Kierowca'),
        ),
        migrations.AlterField(
            model_name='truck',
            name='plate_number',
            field=models.CharField(max_length=8, verbose_name='Numer rejestracyjny'),
        ),
    ]
