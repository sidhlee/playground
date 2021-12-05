from rest_framework import serializers
from .models import Instrument, Musician, Genre, Album, Track


class InstrumentSerializer(serializers):
    class Meta:
        model = Instrument
        fields = "__all__"


class MusicianSerializer(serializers):
    class Meta:
        model = Musician
        fields = "__all__"


class GenreSerializer(serializers):
    class Meta:
        model = Genre
        fields = "__all__"


class AlbumSerializer(serializers):
    class Meta:
        model = Album
        fields = "__all__"


class TrackSerializer(serializers):
    class Meta:
        model = Track
        fields = "__all__"
