from django.db import models
from django.contrib.auth.models import User


class Owner(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=100)
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
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null= True)
    creator = models.ForeignKey('auth.User', related_name='dogs', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']


class Event(models.Model):
    title = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True)
    creator = models.ForeignKey('auth.User', related_name='events', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']



