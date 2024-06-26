# Generated by Django 4.2.1 on 2023-11-30 20:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LibraryApp", "0011_alter_book_authors"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="creation_dates",
            field=models.IntegerField(
                help_text="Entrez l'année",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1000),
                    django.core.validators.MaxValueValidator(2100),
                ],
                verbose_name="Dates de parution",
            ),
        ),
    ]
