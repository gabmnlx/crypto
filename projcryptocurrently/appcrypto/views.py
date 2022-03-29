from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from coin_details import getCoinDesc, curValue, shortName

from datetime import datetime, date
import calendar

# Create your views here.

def homepageview(request):
    context = {}
    context['date'] = datetime.date(datetime.now())
    context['time'] = datetime.time(datetime.now())
    context['day'] = calendar.day_name[date.today().weekday()]
    
    return render(request, 'index.html', context)

def coinview(request, coin_name):
    context = {}
    context['coin_name'] = coin_name.capitalize()
    context['coin_description'] = getCoinDesc(coin_name)
    context['value'] = curValue(coin_name)
    context['short'] = shortName(coin_name)

    return render(request, 'coin.html', context)
