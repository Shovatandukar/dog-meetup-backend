from django_filters import rest_framework as filters
from .models import Dog


# We create filters for each field we want to be able to filter on
class DogFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    breed = filters.CharFilter(lookup_expr='icontains')
    weight = filters.NumberFilter()
    creator__username = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Dog
        fields = ['name', 'breed', 'weight', 'creator__username']

