# Generated by Django 4.0.4 on 2022-05-12 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0013_alter_party_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='is_attending',
        ),
        migrations.AddField(
            model_name='party',
            name='attending',
            field=models.IntegerField(default=0, verbose_name='# Attending'),
        ),
    ]
