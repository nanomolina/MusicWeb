from django.conf.urls import patterns, include, url
from apps.interpreter.views import show_bands, add_band, add_artist

urlpatterns = patterns(
    '',
    url(r'^show_bands/$', show_bands, name='show_bands'),
    url(r'^add_band/$', add_band, name='add_band'),
    url(r'^add_artist/$', add_artist, name='add_artist'),
)
