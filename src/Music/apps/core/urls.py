from django.conf.urls import patterns, include, url
from apps.core.views import home, sign_up

urlpatterns = patterns(
    '',
    url(r'^$', home, name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/login/'}, name='logout'),
    url(r'^signup/$', sign_up, name='sign_up'),
)
