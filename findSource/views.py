#from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from findSource.AlchemyTest.alchemytest import readArticle

# Create your views here.

class IndexView(TemplateView):
    template_name = 'findSource/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

class ResultView(ListView):
    template_name = 'findSource/result.html'

    def get_queryset(self):
        url = self.kwargs['userInput']
        list = readArticle(url)
        #print list
        return list

    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        user_input = self.kwargs['userInput']
        context['userInput'] = user_input
        return context

class AboutView(TemplateView):
    template_name = 'findSource/about.html'
