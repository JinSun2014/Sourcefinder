from django.conf.urls import patterns, include, url

from django.contrib import admin

#from Sourcefinder import settings
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Sourcefinder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^findSource/', include('findSource.urls', namespace = 'findSource')),
)

urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^findSource/static/(?P<path>.*)$', 'serve'),
    )

