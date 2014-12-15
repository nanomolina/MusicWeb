from django.contrib import admin
from apps.interpreter.models import *


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'origin')
    search_fields = ('name',)


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('artistic_name', 'birthday', 'place_of_birth')


admin.site.register(Band, BandAdmin)
admin.site.register(Artist, ArtistAdmin)
