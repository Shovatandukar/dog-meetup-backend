from rest_framework import serializers
from .models import Dog, Event, Owner

from django.contrib.auth.models import User


class DogSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Dog
        fields = ('id', 'name', 'breed', 'weight', 'creator')


class EventSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Event
        fields = ('id', 'title', 'activity', 'location', 'creator')


class OwnerSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')
    owner = EventSerializer(read_only=True, many=True)

    class Meta:
        model = Owner
        fields = ('id', 'first_name', 'last_name', 'address', 'email', 'phone', 'creator', 'dogs', 'events')

