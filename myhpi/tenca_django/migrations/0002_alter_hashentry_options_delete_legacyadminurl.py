# Generated by Django 4.0.7 on 2022-09-15 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tenca_django", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="hashentry",
            options={
                "verbose_name": "Mailing List Hash Entry",
                "verbose_name_plural": "Mailing List Hash Entries",
            },
        ),
        migrations.DeleteModel(
            name="LegacyAdminURL",
        ),
    ]