# Generated by Django 3.1.5 on 2021-01-18 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0009_auto_20210117_0316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='details',
        ),
    ]
