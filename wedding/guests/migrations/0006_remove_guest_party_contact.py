# Generated by Django 3.1.5 on 2021-01-17 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0005_auto_20210117_0122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='party_contact',
        ),
    ]
