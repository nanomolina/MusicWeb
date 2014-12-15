from django.db import models
from apps.interpreter.models import Band, Artist
from apps.album.constants import GENRES


class Album(models.Model):
    title = models.CharField(max_length=60)
    number = models.PositiveIntegerField(max_length=2)
    band = models.ForeignKey(Band, related_name='albums')
    genre = models.IntegerField(max_length=3, choices=GENRES)
    tracks_numbers = models.PositiveIntegerField(max_length=2)
    date = models.DateField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='apps/album/static/album/img',
                              null=True, blank=True)

    def year(self):
        try:
            return self.date.year
        except:
            return None

    def image_url(self):
        if self.image != "":
          a, url = self.image.url.split('apps/album')
          response = url
        else:
          response = ""
        return response

    def __unicode__(self):
        return "%s" % (self.title,)


class Track(models.Model):
    title = models.CharField(max_length=60)
    album = models.ForeignKey(Album, related_name='tracks')
    number = models.PositiveIntegerField(null=True, blank=True)
    duration = models.TimeField(null=True, blank=True)
    composers = models.ManyToManyField(Artist, related_name='tracks',
                                       null=True, blank=True)
    lyric = models.TextField(null=True, blank=True)

    @property
    def interpreter(self):
        return self.album.band

    def __unicode__(self):
        return "%s" % (self.title,)
