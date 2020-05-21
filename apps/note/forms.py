from .models import Note
from django import forms


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['text']
        widgets = {
            "text" : forms.Textarea(attrs={"class":"form-control textarea",'placeholder':"Add notes",}),
        }
        labels = {
            "text": '',
        }
        
