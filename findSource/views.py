from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#def class IndexView(templateView):

def index(request):
    return HttpResponse('Hello, this is SourceFinder')

