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

    class Meta:
        model = Owner
        fields = ('id', 'first_name', 'last_name', 'address', 'email', 'phone', 'creator')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    dogs = serializers.PrimaryKeyRelatedField(many=True, queryset=Dog.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'dogs')
