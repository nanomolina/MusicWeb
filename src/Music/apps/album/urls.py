from django.conf.urls import patterns, include, url
from apps.album.views import *

urlpatterns = patterns(
    '',
    url(r'^show_albums/$', show_albums, name='show_albums'),
    url(r'^(?P<album_id>\d+)/show_tracks/$',
        show_tracks, name='show_tracks'),
    url(r'^add_album/$', add_album, name='add_album'),
    url(r'^add_track/$', add_track, name='add_track'),
)
