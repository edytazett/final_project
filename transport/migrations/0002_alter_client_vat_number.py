# Generated by Django 4.2.1 on 2023-06-04 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='vat_number',
            field=models.CharField(max_length=60, unique=True, verbose_name='Numer NIP'),
        ),
    ]