from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateEventAPIView.as_view(), name='get_post_events'),
    path('<int:pk>/', views.RetrieveUpdateDestroyDogAPIView.as_view(), name='get_delete_update_Dog'),
]