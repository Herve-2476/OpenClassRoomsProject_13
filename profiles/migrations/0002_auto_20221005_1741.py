# Generated by Django 3.0 on 2022-10-05 15:41

from django.db import migrations


def copy_table(apps, schema_editor):
    Profile = apps.get_model("profiles", "Profile")
    Profile_source = apps.get_model("oc_lettings_site", "Profile")
    fields = ["id", "user_id", "favorite_city"]
    for obj in Profile_source.objects.all():
        kwargs = {}
        for field in fields:
            kwargs[field] = obj.__dict__[field]
        Profile(**kwargs).save()


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [migrations.RunPython(copy_table)]
