# Generated by Django 3.1.8 on 2021-11-19 01:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dogs', '0007_auto_20211117_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='event',
            name='owner',
        ),
        migrations.AddField(
            model_name='owner',
            name='lat',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='owner',
            name='lon',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='owner',
            name='phone',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owners', to=settings.AUTH_USER_MODEL),
        ),
    ]
