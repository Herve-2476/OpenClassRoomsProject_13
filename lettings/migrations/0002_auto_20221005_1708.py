# Generated by Django 3.0 on 2022-10-05 15:08

from django.db import migrations


def copy_tables(apps, schema_editor):
    Address = apps.get_model("lettings", "Address")
    Address_source = apps.get_model("oc_lettings_site", "Address")
    fields = ["id", "number", "street", "city", "state", "zip_code", "country_iso_code"]
    for obj in Address_source.objects.all():
        kwargs = {}
        for field in fields:
            kwargs[field] = obj.__dict__[field]
        Address(**kwargs).save()

    Letting = apps.get_model("lettings", "Letting")
    Letting_source = apps.get_model("oc_lettings_site", "Letting")
    fields = ["id", "title", "address_id"]
    for obj in Letting_source.objects.all():
        kwargs = {}
        for field in fields:
            kwargs[field] = obj.__dict__[field]
        Letting(**kwargs).save()


class Migration(migrations.Migration):

    dependencies = [
        ("lettings", "0001_initial"),
    ]

    operations = [migrations.RunPython(copy_tables)]
