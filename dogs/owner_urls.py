from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateOwnerAPIView.as_view(), name='get_post_owners'),
    path('<int:pk>/', views.RetrieveUpdateDestroyOwnerAPIView.as_view(), name='get_delete_update_Owner'),
]