from django.shortcuts import render
from .models import Artist, Songs

# Create your views here.
def homepage(request):
    artist = Artist.objects.all()[:2]
    songs = Songs.objects.all()[:2]
    context = {
        'artist': artist,
        'songs': songs
        }

    return render(request, 'homepage.html',context)

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')

def artists(request):
    artist = Artist.objects.all()
    return render(request, 'artists.html', {'artist': artist})

def songs(request):
    songs = Songs.objects.order_by('-created_at')
    artist = Artist.objects.all()
    context = {
        'songs':songs,
        'artist':artist  
    }
    return render(request, 'songs.html', context)

def contact(request):
    return render(request, 'contact.html')

def artist_details(request, pk):
    artist = Artist.objects.get(id = pk)
    songs = Songs.objects.filter(artists=artist)
    context =  {
        'artist':artist,
        'songs':songs
        }
    return render(request, 'artists_details.html',context)