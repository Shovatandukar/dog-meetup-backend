from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Dog, Event, Owner
from .permissions import IsOwnerOrReadOnly
from .serializers import DogSerializer, EventSerializer, OwnerSerializer
from .pagination import CustomPagination
from .filters import DogFilter


class ListCreateDogAPIView(ListCreateAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DogFilter

    def perform_create(self, serializer):
        # Assign the user who created the movie
        serializer.save(creator=self.request.user)


class ListCreateEventAPIView(ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        # Assign the user who created the movie
        serializer.save(creator=self.request.user)


class ListCreateOwnerAPIView(ListCreateAPIView):
    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        # Assign the user who created the movie
        serializer.save(creator=self.request.user)


class RetrieveUpdateDestroyDogAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class RetrieveUpdateDestroyEventAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class RetrieveUpdateDestroyOwnerAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class DogList(generics.ListAPIView):
    serializer_class = DogSerializer

    def get_queryset(self):
        """
        This view should return a list of all the Dogs
        for the currently authenticated user.
        """
        user = self.request.user
        return Dog.objects.filter(creator=user)


class EventList(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        """
        This view should return a list of all the Events
        for the currently authenticated user.
        """
        user = self.request.user
        return Event.objects.filter(creator=user)


class OwnerDetails(generics.ListAPIView):
    serializer_class = OwnerSerializer

    def get_queryset(self):
        """
        This view should return the Owner Profile
        for the currently authenticated user.
        """
        user = self.request.user
        return Owner.objects.filter(creator=user)
