from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateEventAPIView.as_view(), name='get_post_events'),
    path('filtered', views.EventList.as_view(), name='list_events'),
    path('<int:pk>/', views.RetrieveUpdateDestroyEventAPIView.as_view(), name='get_delete_update_Dog'),
]