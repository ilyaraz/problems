# Create your views here.

from django.http import HttpResponse
from math_notepad.models import Note, Tag
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import datetime

def home(request):
    return show_notes(Note.objects.all().filter(deleted = False))

def tag(request, tag_id):
    return show_notes(Note.objects.filter(deleted = False).filter(tags__id = tag_id))

def note(request, note_id):
    return show_notes(Note.objects.filter(deleted = False).filter(id = note_id))

def add_note(request):
    context = Context({
        'tags': Tag.objects.all(),
    })
    header_1 = loader.get_template('math_notepad/header_1.html')
    add_note_scripts = loader.get_template('math_notepad/add_note_scripts.html')
    header_2 = loader.get_template('math_notepad/header_2.html')
    add_note = loader.get_template('math_notepad/add_note.html')
    footer = loader.get_template('math_notepad/footer.html')
    return HttpResponse(header_1.render(Context()) +
                        add_note_scripts.render(Context()) + 
                        header_2.render(Context()) +
                        add_note.render(context) + 
                        footer.render(Context()))

@csrf_exempt
def add_note_request(request):
    new_note_text = request.POST['text']
    tags = [int(x) for x in request.POST.getlist('tags[]')]
    new_note = Note(text = new_note_text, creation_date = datetime.datetime.now(), deleted = False)
    new_note.save()
    for tag in tags:
        new_note.tags.add(Tag.objects.get(pk = tag))
    new_note.save()
    return HttpResponse("blah!")

def tags(request):
    context = Context({
        'tags': Tag.objects.all(),
    })
    header_1 = loader.get_template('math_notepad/header_1.html')
    tags_scripts = loader.get_template('math_notepad/tags_scripts.html')
    header_2 = loader.get_template('math_notepad/header_2.html')
    tags = loader.get_template('math_notepad/tags.html')
    footer = loader.get_template('math_notepad/footer.html')
    return HttpResponse(header_1.render(Context()) +
                        tags_scripts.render(Context()) + 
                        header_2.render(Context()) +
                        tags.render(context) +
                        footer.render(Context()))

@csrf_exempt
def new_tag(request):
    new_tag_name = request.POST['name']
    new_tag = Tag.objects.create(name = new_tag_name)
    json_serializer = serializers.get_serializer('json')()
    return HttpResponse(json_serializer.serialize(Tag.objects.all(), ensure_ascii = False))

def show_notes(notes):
    context = Context({
        'notes': notes,
    })
    header_1 = loader.get_template('math_notepad/header_1.html')
    header_2 = loader.get_template('math_notepad/header_2.html')
    notes = loader.get_template('math_notepad/notes.html')
    footer = loader.get_template('math_notepad/footer.html')
    return HttpResponse(header_1.render(Context()) +
                        header_2.render(Context()) +
                        notes.render(context) +
                        footer.render(Context()))
