from django.shortcuts import render, redirect, get_object_or_404
from .forms import NoteForm
from .models import Note
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes/note_list.html', {'notes': notes})


@login_required
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user  # привʼязуємо до авторизованого користувача
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/create_note.html', {'form': form})

@login_required
def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/edit_note.html', {'form': form, 'note': note})

@login_required
def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/delete_note.html', {'note': note})

@login_required
def view_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/view_note.html', {'note': note})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # одразу вхід
            return redirect('note_list')
    else:
        form = UserCreationForm()
    return render(request, 'notes/register.html', {'form': form})