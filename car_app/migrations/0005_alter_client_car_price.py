# Generated by Django 4.2.7 on 2023-12-02 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0004_client_car_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_car',
            name='Price',
            field=models.FloatField(),
        ),
    ]