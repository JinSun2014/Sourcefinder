#from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'findSource/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

class ResultView(ListView):
    template_name = 'findSource/result.html'

    def get_queryset(self):
        return [1, 2, 3, 4, 5]

    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        url = self.kwargs['url']
        context['url'] = url
        return context
