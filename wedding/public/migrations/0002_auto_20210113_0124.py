# Generated by Django 3.1.5 on 2021-01-13 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeofinterest',
            name='lat',
            field=models.DecimalField(decimal_places=6, help_text='Use <a href="https://www.latlong.net/convert-address-to-lat-long.html" target="_blank">this</a> to get values', max_digits=9),
        ),
        migrations.AlterField(
            model_name='placeofinterest',
            name='long',
            field=models.DecimalField(decimal_places=6, help_text='Use <a href="https://www.latlong.net/convert-address-to-lat-long.html" target="_blank">this</a> to get values', max_digits=9),
        ),
    ]
