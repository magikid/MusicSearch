from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import ArtistSerializer, BandSerializer, AlbumSerializer

from .models import Band, Artist, Album

class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class BandViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Band.objects.all()
    serializer_class = BandSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


def home(request):
    all_bands = Band.objects.all()
    return render(request, 'band_list.html', {
        'bands': all_bands,
    })


#Detail Views for all 3 Models
def band_detail(request, band_id):
    get_band = Band.objects.get(id=band_id)
    return render(request, 'BandDetail.html', {
        'bands': get_band,
    })


def artist_detail(request, artist_id):
    get_artist = Artist.objects.get(id=artist_id)
    return render(request, 'ArtistDetail.html', {
        'artists': get_artist,
    })


def album_detail(request, album_id):
    get_album = Album.objects.get(id=album_id)
    return render(request, 'AlbumDetail.html', {
        'albums': get_album,
    })


#List Views for all 3 Models
def band_list(request):
    get_band = Band.objects.all()
    print(get_band)
    return render(request, 'band_list.html', {
        'bands': get_band,
    })


def artist_list(request):
    get_artist = Artist.objects.all()
    print(get_artist)
    return render(request, 'artist_list.html', {
        'artists': get_artist,
    })


def album_list(request):
    get_album = Album.objects.all()
    print(get_album)
    return render(request, 'album_list.html', {
        'albums': get_album,
    })


