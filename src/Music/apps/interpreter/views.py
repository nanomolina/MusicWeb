# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, HttpResponse
from django.template import RequestContext
from django.shortcuts import redirect
from apps.interpreter.models import *
from apps.interpreter.forms import *


def show_bands(request):
    bands = Band.objects.all().order_by('name')
    context = {'bands': bands}
    return render_to_response('interpreter/bands.html',
                              RequestContext(request,
                                            context)
                             )


@login_required
def add_artist(request):
    """
    Vemos que en el caso de que el método sea POST y el formulario
    no sea válido le devolvemos al usuario el mismo formulario y
    así de esta manera con bootstrap podemos marcarle al usuario
    cuales fueron sus errrores.
    """
    if request.method == "GET":
        form = ArtistForm()
        context = {'artist_form': form}
        return render_to_response('interpreter/artist_form.html',
                                  RequestContext(request,
                                                 context)
                                 )
    elif request.method == "POST":
        print request.POST
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
        return render_to_response(
            'interpreter/artist_form.html',
            RequestContext(request, {'artist_form': form})
        )


@login_required
def add_band(request):
    if request.method == "GET":
        form = BandForm()
        context = {'band_form': form}
        return render_to_response('interpreter/band_form.html',
                                  RequestContext(request,
                                                 context)
                                 )
    elif request.method == "POST":
        print request.POST
        form = BandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
        return render_to_response(
            'interpreter/band_form.html',
            RequestContext(request, {'band_form': form})
        )
