from django.conf.urls import patterns, include, url

from django.contrib import admin

from Sourcefinder import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Sourcefinder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.IndexView.as_view(), name="homepage"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'Sourcerous/', include('findSource.urls', namespace = 'findSource')),
)

urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )

