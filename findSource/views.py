#from django.shortcuts import render
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
        list = []
        urls = self.request.session['url']
        urllist = urls[:-1].split(';')
        for url in urllist:
            list.append(readArticle(url))
        return list

        '''url = self.request.session['url']
        list = readArticle(url)
        print list
        return list'''

    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        #context.update(csrf(self.request))
        user_input = self.kwargs['userInput']
        context['userInput'] = user_input
        return context

class AboutView(TemplateView):
    template_name = 'findSource/about.html'
