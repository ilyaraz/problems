# Create your views here.

from django.http import HttpResponse
from math_notepad.models import Note, Tag
from django.template import Context, loader

def home(request):
    return show_notes(Note.objects.all())

def tag(request, tag_id):
    return show_notes(Note.objects.filter(tags__id__exact = tag_id))

def note(request, note_id):
    return show_notes(Note.objects.filter(id = note_id))

def show_notes(notes):
    template = loader.get_template('math_notepad/index.html')
    context = Context({
        'notes': notes,
    })
    return HttpResponse(template.render(context))
