# Generated by Django 4.2.1 on 2023-11-28 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LibraryApp", "0003_rename_last_name_author_username_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="registration_date",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Date d'enregistrement"
            ),
        ),
    ]