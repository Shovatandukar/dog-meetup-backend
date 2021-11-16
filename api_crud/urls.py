
from django.contrib import admin
from django.urls import include, path

# urls
urlpatterns = [
    path('api/v1/dogs/', include('dogs.urls')),
    path('api/v1/events/', include('dogs.events_urls')),
    path('api/v1/auth/', include('authentication.urls')),
    path('api/v1/owners/', include('dogs.owner_urls')),
    path('admin/', admin.site.urls),
]