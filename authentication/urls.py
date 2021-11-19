from django.urls import path
from .views import RegisterView, RetrieveUpdateDestroyUserAPIView, current_user
from .serializers import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('users/', UserViewSet.as_view({'get': 'list'}), name='auth_register'),
    path('users/<int:pk>/', RetrieveUpdateDestroyUserAPIView.as_view(), name='get_delete_update_Dog'),
    path('currentuser/', current_user, name='auth_register'),

]