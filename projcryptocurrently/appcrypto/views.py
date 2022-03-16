from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from coin_details import getCoinDesc, curValue

# Create your views here.

def homepageview(request):
    return render(request, 'index.html')

def coinview(request, coin_name):
    context = {}
    context['coin_name'] = coin_name.capitalize()
    context['coin_description'] = getCoinDesc(coin_name)
    context['value'] = curValue(coin_name)

    return render(request, 'coin.html', context)
