# Generated by Django 4.0 on 2023-02-18 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('noid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('tipo', models.CharField(max_length=10)),
                ('region', models.CharField(max_length=100)),
                ('tipologia', models.CharField(max_length=10)),
                ('titular', models.CharField(max_length=100)),
                ('inversion', models.FloatField()),
                ('fechapresentacion', models.DateField()),
                ('estado', models.CharField(max_length=100)),
                ('mapa', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
