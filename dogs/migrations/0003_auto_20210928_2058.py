# Generated by Django 3.1.8 on 2021-09-28 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dogs', '0002_auto_20210928_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dogs', to=settings.AUTH_USER_MODEL),
        ),
    ]
