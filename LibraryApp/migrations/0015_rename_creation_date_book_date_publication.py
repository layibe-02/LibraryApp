# Generated by Django 4.2.1 on 2023-11-30 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("LibraryApp", "0014_remove_book_creation_dates_book_creation_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book", old_name="creation_date", new_name="date_publication",
        ),
    ]
