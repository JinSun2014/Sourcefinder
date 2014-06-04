#! /usr/bin/env python2.7.6
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from findSource import views

urlpatterns = patterns('',
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^about$', views.AboutView.as_view(), name = 'about'),
        url(r'(?P<userInput>.*)/result', views.MultiThreadResultView.as_view(), name = 'result'),
        #url(r'^getInfo$', views.GetInfoView.as_view(), name='GetInfo'),
        #url(r'^(?P<userInput>.*)/urls$', views.URLsView.as_view(), name='urls'),
        #url(r'^(?P<userInput>.*)/result$', views.ResultsView.as_view(), name='result'),
        #url(r'^(?P<userInput>.*)/result$', views.ResultView.as_view(), name='result'),
        #url(r'^(?P<userInput>.*)$', views.LinksView.as_view(), name='links'),
)

urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^/static/(?P<path>.*)$', 'serve'),
    )

