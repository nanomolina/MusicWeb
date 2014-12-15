# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, HttpResponse
from django.template import RequestContext
from django.shortcuts import redirect
from apps.album.models import *
from apps.album.forms import *

"""
La mayoria de las vistas tienen la misma estructura al igual
que los html's. Básicamente buscan y arman un contexto y se
lo envían al usuario.
"""
def show_albums(request):
    albums = Album.objects.all().order_by('number')
    context = {'albums': albums}
    return render_to_response('album/albums.html',
                              RequestContext(request, context))


def show_tracks(request, album_id):
    album = Album.objects.get(id=album_id)
    tracks = Track.objects.filter(album=album).order_by('number')
    context = {'tracks': tracks}
    return render_to_response('album/tracks.html',
                              RequestContext(request, context))


"""
Vemos que en el caso de que el método sea POST y el formulario
no sea válido le devolvemos al usuario el mismo formulario y
así de esta manera con bootstrap podemos marcarle al usuario
cuales fueron sus errrores.
"""
@login_required
def add_album(request):
    if request.method == "GET":
        form = AlbumForm()
        context = {'album_form': form}
        return render_to_response('album/album_form.html',
                                  RequestContext(request, context))
    elif request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
        context = {'album_form': form}
        return render_to_response('album/album_form.html',
                                  RequestContext(request, context))


@login_required
def add_track(request):
    if request.method == "GET":
        form = TrackForm()
        context = {'track_form': form}
        return render_to_response('album/track_form.html',
                                  RequestContext(request, context))
    elif request.method == "POST":
        print request.POST
        form = TrackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
        context = {'track_form': form}
        return render_to_response('album/track_form.html',
                                  RequestContext(request, context))
