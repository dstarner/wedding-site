# Generated by Django 4.0.4 on 2022-05-16 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0016_alter_guest_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='requests',
            field=models.TextField(default='', help_text='Allergies and special requests'),
        ),
    ]
