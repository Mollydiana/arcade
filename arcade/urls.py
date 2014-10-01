from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'games.views.home', name='home'),
    url(r'^paint/', 'games.views.paint', name='paint'),
    url(r'^snake/', 'games.views.snake', name='snake'),

    url(r'^admin/', include(admin.site.urls)),
)
