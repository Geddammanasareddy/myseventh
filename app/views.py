from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('<h1><marquee>data that we have to respond</marquee></h1>')
