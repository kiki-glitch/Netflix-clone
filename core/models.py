from django.db import models
from django.conf import settings
import uuid


# Create your models here.

class Movie(models.Model):

    GENRE_CHOICES = [
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('science_fiction', 'Science Fiction'),
        ('fantasy', 'Fantasy'),
    ]

    TYPE_CHOICES = [
        ('movie', 'Movie'),
        ('series', 'Series')
    ]

    uuid = models.UUIDField(default=uuid.uuid4)
    title = models.CharField(max_length = 255)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    length = models.PositiveIntegerField()
    image_card = models.ImageField(upload_to='movie_images/')
    image_cover = models.ImageField(upload_to='movie_images/')
    video = models.FileField(upload_to='movie_videos')
    movie_views = models.IntegerField(default=0)

     # New fields
    is_featured = models.BooleanField(default=False)
    trailer = models.URLField(blank=True, null=True)
    actors = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=100, blank=True)
    subtitles = models.CharField(max_length=255, blank=True)
    rating = models.FloatField(default=0.0)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='series')
    tagline = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title

class MovieList(models.Model):
    owner_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

