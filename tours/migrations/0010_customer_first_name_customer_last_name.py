# Generated by Django 5.0.6 on 2024-07-16 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0009_remove_user_bio_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]