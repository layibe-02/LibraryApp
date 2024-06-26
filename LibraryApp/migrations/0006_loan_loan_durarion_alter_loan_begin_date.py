# Generated by Django 4.2.1 on 2023-11-28 20:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("LibraryApp", "0005_customer_registration_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="loan",
            name="loan_durarion",
            field=models.IntegerField(default=14, verbose_name="Durée de prêt"),
        ),
        migrations.AlterField(
            model_name="loan",
            name="begin_date",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Date d'emprunt"
            ),
        ),
    ]
