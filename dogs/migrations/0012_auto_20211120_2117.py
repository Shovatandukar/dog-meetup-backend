# Generated by Django 3.1.8 on 2021-11-20 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0011_auto_20211120_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='dogType',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='eventDate',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
