from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from rest_framework import generics, response
from rest_framework.views import APIView



from simple_app.serializers import NoteSerializer

from .forms import NoteForm
from .models import Note


class NotesIndexView(View):
    # render start page
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
        }
        return render(request, 'simple_app/note_index.html', context=context)


class NoteDetailView(DetailView):
    # page with information about single note
    template_name = "simple_app/note_details.html"
    model = Note
    context_object_name = "note"

class NotesListView(ListView):
    # page with list of all notes (not archived)
    template_name = "simple_app/notes_list.html"
    context_object_name = "notes"
    queryset = Note.objects.filter(archived=False)

class NoteCreateView(CreateView):
    # create new note, user input label and text
    model = Note
    fields = "label", "text"
    success_url = reverse_lazy("simple_app:notes_list")


class NoteUpdateView(UpdateView):
    # update notes
    model = Note
    template_name = "simple_app/note_update_form.html"
    form_class = NoteForm

    def get_success_url(self):
        return reverse("simple_app:notes_list")


class NoteApiView(generics.ListAPIView):
    # return all notes
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteCountApiView(APIView):
    # return count of all notes
    def get(self, request):
        note_count = Note.objects.count()
        content = {'note_count': note_count}
        return response.Response(content)
