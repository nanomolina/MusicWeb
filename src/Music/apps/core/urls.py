from django.conf.urls import patterns, include, url
from apps.core.views import home, login

urlpatterns = patterns(
    '',
    url(r'^$', home, name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^login_user/$', login, name='login_user'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/login/'}, name='logout'),
)
