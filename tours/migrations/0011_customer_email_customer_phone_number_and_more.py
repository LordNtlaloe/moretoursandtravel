# Generated by Django 5.0.6 on 2024-07-16 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0010_customer_first_name_customer_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(default=0, max_length=15),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
