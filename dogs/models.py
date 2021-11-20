from django.db import models
from django.contrib.auth.models import User


class Owner(models.Model):
    creator = models.ForeignKey('auth.User', related_name='owners', on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, null=True)
    lat = models.CharField(max_length=100, null=True)
    lon = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']


class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    weight = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey('auth.User', related_name='dogs', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']


class Event(models.Model):
    title = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    lat = models.CharField(max_length=100, null=True)
    lon = models.CharField(max_length=100, null=True)
    eventDate = models.CharField(max_length=100, null=True)
    dogType = models.CharField(max_length=100, null=True)
    attendees = models.CharField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey('auth.User', related_name='events', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']



