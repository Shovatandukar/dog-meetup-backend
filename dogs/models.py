from django.db import models


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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey('auth.User', related_name='events', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']


class Owner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dogs = models.ManyToManyField(Dog, related_name="owners_dogs")
    events = models.ManyToManyField(Event, related_name="owners_event")
    creator = models.ForeignKey('auth.User', related_name='owners', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']
