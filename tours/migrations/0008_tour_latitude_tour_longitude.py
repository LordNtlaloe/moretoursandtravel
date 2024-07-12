# Generated by Django 5.0.6 on 2024-06-26 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0007_tour_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='latitude',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='longitude',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
    ]
