from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm, NoteForm


# Create your views here.
def list_albums(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html", 
                  {"albums": albums})


def add_album(request):
    if request.method == 'GET':
        form = albumForm()
    else:
        form = albumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "albums/add_album.html", {"form": form})


def edit_album(request, pk):
    album = get_object_or_404(album, pk=pk)
    if request.method == 'GET':
        form = albumForm(instance=album)
    else:
        form = albumForm(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "albums/edit_album.html", {
        "form": form,
        "album": album
    })

def add_note(request, pk):
    album = get_object_or_404(album, pk=pk)
    if request.method == 'GET':
        form = NoteForm()
    else:
        form = NoteForm(data=request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.album = album
            new_note.save()
            return redirect(to='list_albums')

    return render(request, "albums/add_note.html", {
        "form": form,
        "album": album
    })


def delete_album(request, pk):
    album = get_object_or_404(album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_albums')

    return render(request, "albums/delete_album.html",
                  {"album": album})

def view_album(request, pk):
    album = get_object_or_404(album, pk=pk)
    return render(request, 'albums/view_album.html', {"album": album})
    
