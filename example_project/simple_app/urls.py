from django.contrib import admin
from django.urls import path, include
from .views import index, NotesListView, NoteCreateView

app_name = "simple_app"

urlpatterns = [
    path("", index, name="index"),
    path("list/", NotesListView.as_view(), name="notes_list"),
    path("create/", NoteCreateView.as_view(), name="note_create"),
]