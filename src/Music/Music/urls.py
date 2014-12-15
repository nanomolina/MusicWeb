from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.core.urls', namespace='core')),
    url(r'^interpreter/', include('apps.interpreter.urls',
                                   namespace='interpreter')),
    url(r'^album/', include('apps.album.urls', namespace='album')),
)