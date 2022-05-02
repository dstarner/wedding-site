# Generated by Django 4.0.4 on 2022-05-02 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0011_auto_20210302_0408'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='code',
            field=models.CharField(default='', help_text='Unique code that identifies the party', max_length=4, verbose_name='Party Code'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='guests.party'),
        ),
    ]