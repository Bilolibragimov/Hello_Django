from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def my_world(request):
    data = 'Hello World!'
    return HttpResponse(data)