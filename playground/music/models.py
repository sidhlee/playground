from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from common.custom_fields import LowerCharField


def validate_rating(rating):
    if 0 <= rating <= 100:
        return
    raise ValidationError("Rating should be between 0 and 100, inclusive.")


class Instrument(models.Model):
    name = LowerCharField(max_length=50)

    def __str__(self):
        return self.name


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.ManyToManyField(Instrument)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = LowerCharField(max_length=50)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    date_released = models.DateField()
    rating = models.IntegerField(validators=[validate_rating])

    def __str__(self):
        return self.title


class Track(models.Model):
    title = models.CharField(max_length=50)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    main_artists = models.ManyToManyField(Musician)
    featured_artists = models.ManyToManyField(Musician, related_name="featured_tracks")
    track_number = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    lyrics = models.TextField(blank=True)
    duration = models.DurationField()
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
