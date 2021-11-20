from rest_framework import serializers, generics
from .models import Dog, Event, Owner
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


class DogSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Dog
        fields = ('id', 'name', 'breed', 'weight', 'creator')


class EventSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Event
        fields = ('id', 'title', 'activity', 'location', 'lat', 'lon', 'eventDate', 'dogType', 'attendees', 'creator')


class OwnerSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Owner
        fields = ('id', 'creator', 'address', 'phone', 'first_name', 'last_name', 'email', 'lat', 'lon')



