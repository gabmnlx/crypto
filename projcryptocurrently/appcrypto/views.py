from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from coin_details import getCoinDesc, curValue, shortName, getFluctuation

from datetime import datetime, date
import calendar

# Create your views here.

def homepageview(request):
    context = {}
    context['date'] = datetime.date(datetime.now())
    context['time'] = datetime.time(datetime.now())
    context['day'] = calendar.day_name[date.today().weekday()]

    context['bitcoin_value'] = curValue("bitcoin")
    context['ethereum_value'] = curValue("ethereum")
    context['xrp_value'] = curValue("xrp")
    context['usd_value'] = curValue("usdcoin")
    context['bnb_value'] = curValue("binance")
    context['tether_value'] = curValue("tether")

    context['bitcoin_fluc'] = abs(getFluctuation("bitcoin"))
    context['ethereum_fluc'] = abs(getFluctuation("ethereum"))
    context['xrp_fluc'] = abs(getFluctuation("xrp"))
    context['usd_fluc'] = abs(getFluctuation("usdcoin"))
    context['bnb_fluc'] = abs(getFluctuation("binance"))
    context['tether_fluc'] = abs(getFluctuation("tether"))

    context['bitcoin_fluc_sign'] = getFluctuation("bitcoin") >= 0
    context['ethereum_fluc_sign'] = getFluctuation("ethereum") >= 0
    context['xrp_fluc_sign'] = getFluctuation("xrp") >= 0
    context['usd_fluc_sign'] = getFluctuation("usdcoin") >= 0
    context['bnb_fluc_sign'] = getFluctuation("binance") >= 0
    context['tether_fluc_sign'] = getFluctuation("tether") >= 0
    
    return render(request, 'index.html', context)

def coinview(request, coin_name):
    context = {}
    context['coin_name'] = coin_name.capitalize()
    context['coin_description'] = getCoinDesc(coin_name)
    context['value'] = curValue(coin_name)
    context['short'] = shortName(coin_name)

    return render(request, 'coin.html', context)
