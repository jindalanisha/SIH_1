# Generated by Django 2.2 on 2019-04-23 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_auto_20190423_1241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organisationinfo',
            old_name='organisation_name',
            new_name='orgnisation_name',
        ),
    ]
