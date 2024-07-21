# Generated by Django 5.0.6 on 2024-07-19 07:53

from django.db import migrations, models


def update_emails(apps, schema_editor):
    Customer = apps.get_model('tours', 'Customer')
    for customer in Customer.objects.filter(email=''):
        customer.email = f'unique_{customer.id}@example.com'
        customer.save()

class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0011_customer_email_customer_phone_number_and_more'),
    ]

    operations = [
        migrations.RunPython(update_emails),
    ]