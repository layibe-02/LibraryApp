# Generated by Django 4.2.1 on 2023-11-30 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("LibraryApp", "0008_alter_loan_loan_durarion"),
    ]

    operations = [
        migrations.RemoveField(model_name="loan", name="loan_durarion",),
    ]
