# Generated by Django 4.0.1 on 2022-01-14 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0005_rename_passwrd_cutomer_password'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cutomer',
            new_name='Customer',
        ),
    ]
