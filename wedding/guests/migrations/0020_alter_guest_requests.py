# Generated by Django 4.0.4 on 2022-05-22 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0019_party_rsvped_alter_guest_meal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='requests',
            field=models.TextField(blank=True, default='', help_text='Allergies and special requests'),
        ),
    ]
