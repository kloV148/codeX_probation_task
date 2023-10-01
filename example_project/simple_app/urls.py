from django.contrib import admin
from django.urls import path, include
from .views import (
    NotesIndexView,
    NotesListView,
    NoteCreateView,
    NoteUpdateView,
    NoteDetailView,
)

app_name = "simple_app"

urlpatterns = [
    path("", NotesIndexView.as_view(), name="index"),
    path("list/", NotesListView.as_view(), name="notes_list"),
    path("list/<int:pk>/", NoteDetailView.as_view(), name="note_detail"),
    path("list/<int:pk>/update/", NoteUpdateView.as_view(), name="note_update"),
    path("create/", NoteCreateView.as_view(), name="note_create"),
]
