from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.TextField()
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    preview_url = models.TextField(null=True, blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')

    def __str__(self):
        return self.title


class Favorite(models.Model):
    user = models.ForeignKey('auth.User', related_name='favorites')
    song = models.ForeignKey(Song, related_name='favorites')