from rest_framework import viewsets
from .serializers import (
    InstrumentSerializer,
    MusicianSerializer,
    GenreSerializer,
    AlbumSerializer,
    TrackSerializer,
)
from .models import Instrument, Musician, Genre, Album, Track


class InstrumentViewSet(viewsets.ModelViewSet):
    queryset = Instrument.objects.all().order_by("name")
    serializer_class = InstrumentSerializer


class MusicianViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all().order_by("last_name")
    serializer_class = MusicianSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all().order_by("name")
    serializer_class = GenreSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().order_by("-date_released")
    serializer_class = AlbumSerializer


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all().order_by("-album__date_released", "track_number")
    serializer_class = TrackSerializer
