# Generated by Django 3.1.5 on 2021-01-17 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0007_party_second_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='association',
            field=models.CharField(choices=[('family', 'Family'), ('friend', 'Friends'), ('work', 'Work Colleague'), ('fam_friend', 'Family Friend')], default='friend', max_length=16, verbose_name='Association'),
        ),
        migrations.AlterField(
            model_name='party',
            name='tier',
            field=models.IntegerField(choices=[(0, 'Wedding Party'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Fallback')], default=1, verbose_name='Priority Tier'),
        ),
    ]
