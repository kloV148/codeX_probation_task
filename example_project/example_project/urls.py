
from django.contrib import admin
from django.urls import path, include

from simple_app.views import NoteApiView, NoteCountApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("simple_app.urls")),

    path('api/notelist/', NoteApiView.as_view()),
    path('api/notelist/count/', NoteCountApiView.as_view()),
]
