# Generated by Django 4.1.7 on 2023-03-19 12:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Category"},
        ),
    ]
