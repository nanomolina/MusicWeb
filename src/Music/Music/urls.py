# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

"""
Dividimos las urls por cada aplicación para tener mayor organización
"""
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.core.urls', namespace='core')),
    url(r'^interpreter/', include('apps.interpreter.urls',
                                   namespace='interpreter')),
    url(r'^album/', include('apps.album.urls', namespace='album')),
)
