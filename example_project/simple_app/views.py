from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Note


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class NotesListView(ListView):
    template_name = "simple_app/notes_list.html"
    context_object_name = "notes"
    queryset = Note.objects.filter(archived=False)

class NoteCreateView(CreateView):
    model = Note
    fields = "label", "text"
    success_url = reverse_lazy("simple_app:notes_list")