from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'legacy_blog_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^storefront/', 'blog.views.storeFront', name='storeFront'),
    url(r'^paint/', 'blog.views.paint', name='paint'),
    url(r'^snake/', 'blog.views.snake', name='snake'),
    url(r'^pokemon/', 'blog.views.pokemon', name='pokemon'),
    url(r'^maps/', 'blog.views.maps', name='maps'),
    url(r'^tomatoes/', 'blog.views.tomatoes', name='tomatoes'),
)
