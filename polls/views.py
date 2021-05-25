from django.shortcuts import render
#polls app is created for custom management commands and custom middleware
# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")