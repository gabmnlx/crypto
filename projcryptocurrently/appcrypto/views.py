from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def index(request):
    return HttpResponse("Cryptocurrently")

def indexhtmlview(request):
    return render(request, 'index.html')
