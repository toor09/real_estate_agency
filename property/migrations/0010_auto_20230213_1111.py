# Generated by Django 2.2.24 on 2023-02-13 08:11

from django.db import migrations


def add_owners_from_flat_model(apps, schema_editor):
    flat_owners = apps.get_model('property', 'Flat')
    owner = apps.get_model('property', 'Owner')
    for flat_owner in flat_owners.objects.all():
        owner.objects.get_or_create(
            owner=flat_owner.owner,
            owners_phonenumber=flat_owner.owners_phonenumber,
            owner_pure_phone=flat_owner.owner_pure_phone,
        )


def move_backward(apps, schema_editor):
    owner = apps.get_model('property', 'Owner')
    owners = owner.objects.all()
    owners.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20230213_1049'),
    ]

    operations = [
        migrations.RunPython(add_owners_from_flat_model, move_backward),
    ]
