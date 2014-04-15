from django.conf.urls import patterns, url

from findSource import views

urlpatterns = patterns('',
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^(?P<url>\S+)$', views.ResultView.as_view(), name='result'),
)

from django.conf import settings

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
