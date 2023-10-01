from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from .forms import NoteForm
from .models import Note


class NotesIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
        }
        return render(request, 'simple_app/note_index.html', context=context)


class NoteDetailView(DetailView):
    template_name = "simple_app/note_details.html"
    model = Note
    context_object_name = "note"

class NotesListView(ListView):
    template_name = "simple_app/notes_list.html"
    context_object_name = "notes"
    queryset = Note.objects.filter(archived=False)

class NoteCreateView(CreateView):
    model = Note
    fields = "label", "text"
    success_url = reverse_lazy("simple_app:notes_list")


class NoteUpdateView(UpdateView):
    model = Note
    template_name = "simple_app/note_update_form.html"
    form_class = NoteForm

    def get_success_url(self):
        return reverse("simple_app:notes_list")