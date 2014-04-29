from django.conf.urls import patterns, url

from findSource import views

urlpatterns = patterns('',
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^about$', views.AboutView.as_view(), name = 'about'),
        url(r'^(?P<userInput>[a-z|A-Z]+)$', views.LinksView.as_view(), name='links'),
        url(r'^(?P<userInput>[a-z|A-Z]+)/result$', views.ResultView.as_view(), name='result'),
)

urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^/static/(?P<path>.*)$', 'serve'),
    )

