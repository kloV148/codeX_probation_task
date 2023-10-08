from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    # form, that create or update note
    class Meta:
        model = Note
        fields = "label", "text"