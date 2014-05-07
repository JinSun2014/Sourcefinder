#! /usr/bin/env python2.7.6
# -*- coding: utf-8 -*-

import json

from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from findSource.AlchemyTest.alchemytest import readArticle

from findSource.GoogleNews import GoogleNews
from django.core.context_processors import csrf

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
        list = GoogleNews(userInput)
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
        urls = self.request.session['url']
        urllist = urls[:-1].split(';')
        for url in urllist:
            joined_list.append(readArticle(url))
        trim_list = joined_list 
        return trim_list

        '''url = self.request.session['url']
        list = readArticle(url)
        print list
        return list'''

    '''
    Extend the list...

    Example: 
    flatten (list)

    '''
    def flatten(l):
        for el in l:
            if hasattr(el, "__iter__") and not isinstance(el, basestring):
                for sub in flatten(el):
                    yield sub
            else:
                yield el     

    def clean(data_dict):
        data_values=data_dict.values()


        joined_list = [x for x in flatten(data_values)]  
        # print joined_list  
        trim_list = list(set(joined_list))  

        counter_total=Counter(joined_list)  
        # print counter_total  


    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        #context.update(csrf(self.request))
        user_input = self.kwargs['userInput']
        context['userInput'] = user_input
        return context

class AboutView(TemplateView):
    template_name = 'findSource/about.html'
