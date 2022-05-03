from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from coin_details import getCoinDesc, curValue, shortName, getFluctuation, eurToUsdConvert, coin_dtm, coin_ngram,coin_tfidf,coin_wordcloud

from sentiment_analyzer.extraction import create_var, create_api, search_to_df, search_tweets
from sentiment_analyzer.cleaner import clean
from sentiment_analyzer.analyzer import analyzerOutput


from datetime import datetime, date
import calendar

# Extraction
import tweepy
import pandas as pd
consumer_key, consumer_key_secret, access_token, access_token_secret = create_var()
def extract(consumer_key, consumer_key_secret, access_token, access_token_secret):
    coin = ["Bitcoin","BNB","Ethereum","Tether","USD Coin","XRP"]
    for x in range(0,len(coin)):
        api = create_api(consumer_key, consumer_key_secret, access_token, access_token_secret)
        search_results = search_tweets(api,coin[x], ignore_rt=True, max_tweets=400)
        tweets = search_to_df(search_results)
        tweets.to_csv("../sentiment_analyzer/out/" + coin[x] + ".csv", index=False)
        # print("Extracting " + coin[x] + " tweets")

t=datetime.now()
if t.minute==46:
    consumer_key, consumer_key_secret, access_token, access_token_secret = create_var()
    print("yo")
    extract(consumer_key, consumer_key_secret, access_token, access_token_secret)


# Create your views here.

def homepageview(request):
    context = {}
    # now = datetime.now()
    # day = now.strftime("%m/%d")
    # time = now.strftime("%H:%M")
    # context['date'] = day
    # context['time'] = time
    context['day'] = calendar.day_name[date.today().weekday()]
    context['conversionRate'] = eurToUsdConvert()

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
    output = analyzerOutput(coin_name)
    context = {}
    context['conversionRate'] = eurToUsdConvert()
    context['positive'] = round(output[0], 2)
    context['negative'] = round(output[1], 2)
    context['compound_score'] = round(output[2], 2)
    context['coin_name'] = coin_name.capitalize()
    context['coin_description'] = getCoinDesc(coin_name)
    context['value'] = curValue(coin_name)
    context['short'] = shortName(coin_name)
    context['coin_dtm'] = coin_dtm(coin_name)
    context['coin_ngram'] = coin_ngram(coin_name)
    context['coin_tfidf'] = coin_tfidf(coin_name)
    context['coin_wordcloud'] = coin_wordcloud(coin_name)

    return render(request, 'coin.html', context)
