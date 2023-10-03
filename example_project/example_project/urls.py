
from django.contrib import admin
from django.urls import path, include

from simple_app.views import NoteApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("simple_app.urls")),
    path('', include('django_prometheus.urls')),

    path('api/notelist/', NoteApiView.as_view()),
]
