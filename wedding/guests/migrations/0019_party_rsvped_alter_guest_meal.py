# Generated by Django 4.0.4 on 2022-05-16 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0018_alter_guest_id_alter_party_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='rsvped',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='guest',
            name='meal',
            field=models.CharField(blank=True, choices=[('chicken', 'Chicken'), ('steak', 'steak'), ('vegetarian', 'Vegetarian Pasta')], max_length=12, null=True),
        ),
    ]