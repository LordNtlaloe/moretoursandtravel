# Generated by Django 5.0.6 on 2024-06-26 07:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0006_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tours.destination'),
        ),
    ]
