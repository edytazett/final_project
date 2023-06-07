# Generated by Django 4.2.1 on 2023-06-05 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0007_remove_order_client_vat_number_order_client'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Client',
            new_name='Customer',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='client',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='client_contact_person',
            new_name='customer_contact_person',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='client_order_number',
            new_name='customer_order_number',
        ),
    ]
