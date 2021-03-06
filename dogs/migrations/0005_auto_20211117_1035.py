# Generated by Django 3.1.8 on 2021-11-16 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0004_event_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='dogs',
            field=models.ManyToManyField(related_name='owners_dogs', to='dogs.Dog'),
        ),
        migrations.AddField(
            model_name='owner',
            name='events',
            field=models.ManyToManyField(related_name='owners_event', to='dogs.Event'),
        ),
    ]
