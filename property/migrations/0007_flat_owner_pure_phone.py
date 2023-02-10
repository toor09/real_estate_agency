# Generated by Django 2.2.24 on 2023-02-10 15:26

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_flat_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Нормализованный номер владельца'),
        ),
    ]
