from django.contrib import admin
from apps.album.models import *


class AlbumInLine(admin.TabularInline):
    model = Track
    extra = 0


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'band', 'genre', 'tracks_numbers', 'year')
    search_field = ('title',)
    inlines = [AlbumInLine]


class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'interpreter', 'duration')


admin.site.register(Album, AlbumAdmin)
admin.site.register(Track, TrackAdmin)
