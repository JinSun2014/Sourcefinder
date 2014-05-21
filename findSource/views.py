#! /usr/bin/env python2.7.6
# -*- coding: utf-8 -*-

import json

from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.utils.encoding import smart_str as _
from django.core.context_processors import csrf

from findSource.AlchemyTest.alchemytest import readArticle
from findSource.GoogleNews import GoogleNews
from findSource.YahooFinance import YahooFinance
from findSource.wiki import wiki

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class JSONResponseMixin(object):
#    def render_to_response(self, context):
#        "Returns a JSON response containing 'context' as payload"
#        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context)

class IndexView(TemplateView):
    template_name = 'findSource/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

class LinksView(ListView):
    template_name = 'findSource/links.html'

    def get_queryset(self):
        userInput = self.kwargs['userInput']
        list = {}
        list['Google News'] = GoogleNews(userInput)
        list['Yahoo Finance'] = YahooFinance(userInput)
        list['Wikipedia'] = wiki(userInput)
        return list

    def get_context_data(self, **kwargs):
        context = super(LinksView, self).get_context_data(**kwargs)
        user_input = self.kwargs['userInput']
        context['userInput'] = user_input
        return context

class ResultView(ListView, JSONResponseMixin):
    template_name = 'findSource/result.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            if request.method == 'POST':
                url = self.request.POST.get('url', '')
                self.request.session['url'] = url
                return self.get_json_response(self.convert_context_to_json({'success': True}))


    def get_queryset(self):
        joined_list = []
        trim_list = []
        #urls = self.request.session['url']

        userInput = self.kwargs['userInput']
        list = {}
        list['Google News'] = GoogleNews(userInput)[:3]
        list['Yahoo Finance'] = YahooFinance(userInput)[:3]
        list['Wikipedia'] = wiki(userInput)[:]

        result = {}
        for (site, info) in list.iteritems():
            joined_list = []
            for item in info:
                result_dict=readArticle(item['url'])
                result_dict['original_source']=item['original_source']
                joined_list.append(result_dict)
            #clean data
            trim_list = joined_list
            # for text in trim_list:
            #     text['author'] =_(text['author'])
            #     text['title'] = unicode(text['title'])
            #     for p in text['people']:
            #         p['name'] = (p['name']).encode('utf-8')
            #         p['quotation'] = unicode(p['quotation'])
            #         p['job_title'] = unicode(p['job_title'])
            result[site] = trim_list

        return result

    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        #context.update(csrf(self.request))
        user_input = self.kwargs['userInput']
        context['userInput'] = user_input
        return context

class AboutView(TemplateView):
    template_name = 'findSource/about.html'
