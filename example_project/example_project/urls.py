
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("simple_app.urls")),
    path('', include('django_prometheus.urls')),
]
