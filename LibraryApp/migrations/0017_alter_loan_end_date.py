# Generated by Django 4.2.1 on 2023-11-30 21:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LibraryApp", "0016_alter_book_registration_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="loan",
            name="end_date",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 12, 3, 21, 39, 5, 760029, tzinfo=datetime.timezone.utc
                ),
                null=True,
                verbose_name="Delai",
            ),
        ),
    ]
