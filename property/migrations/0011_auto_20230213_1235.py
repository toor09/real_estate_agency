# Generated by Django 2.2.24 on 2023-02-13 09:35

from django.apps.registry import Apps
from django.db import migrations
from django.db.backends.base.schema import BaseDatabaseSchemaEditor


def add_flats_to_owner_model(apps: Apps, schema_editor: BaseDatabaseSchemaEditor) -> None:
    flat_owners = apps.get_model('property', 'Flat')
    owner = apps.get_model('property', 'Owner')

    for owner in owner.objects.all():
        owner_flats = flat_owners.objects.filter(
            owner=owner.owner,
            owners_phonenumber=owner.owners_phonenumber,
            owner_pure_phone=owner.owner_pure_phone,
        )
        for owner_flat in owner_flats:
            owner.flats.add(owner_flat)
            owner.save()


def move_backward(apps: Apps, schema_editor: BaseDatabaseSchemaEditor) -> None:
    flat_owners = apps.get_model('property', 'Flat')
    owner = apps.get_model('property', 'Owner')

    for owner in owner.objects.all():
        owner_flats = flat_owners.objects.filter(
            owner=owner.owner,
            owners_phonenumber=owner.owners_phonenumber,
            owner_pure_phone=owner.owner_pure_phone,
        )
        for owner_flat in owner_flats:
            owner.flats.remove(owner_flat)
            owner.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20230213_1111'),
    ]

    operations = [
        migrations.RunPython(add_flats_to_owner_model, move_backward),
    ]
