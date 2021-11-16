from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateDogAPIView.as_view(), name='get_post_dogs'),
    path('<int:pk>/', views.RetrieveUpdateDestroyDogAPIView.as_view(), name='get_delete_update_Dog'),
]