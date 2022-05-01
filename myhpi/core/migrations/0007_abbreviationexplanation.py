# Generated by Django 3.1.8 on 2021-04-14 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_auto_20210414_2113"),
    ]

    operations = [
        migrations.CreateModel(
            name="AbbreviationExplanation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("abbreviation", models.CharField(max_length=255)),
                ("explanation", models.CharField(max_length=255)),
            ],
        ),
    ]