from django.conf.urls import patterns, url

from findSource import views

urlpatterns = patterns('',
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^(?P<url>\S+)$', views.ResultView.as_view(), name='result'),
)
