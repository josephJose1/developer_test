# Generated by Django 4.0 on 2023-02-17 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0002_network_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='network',
            old_name='Company',
            new_name='company',
        ),
    ]
