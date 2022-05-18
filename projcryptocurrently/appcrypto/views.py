from codecs import BOM_BE
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from coin_details import getCoinDesc, curValue, shortName, eurToUsdConvert, coin_dtm, coin_ngram,coin_tfidf,coin_wordcloud,getCompScoreFluctuation
from coin_details import filterCoins, findPositiveAndNegativeFlucs, getCoinsWithMorePositiveSentimentsThanNegative, getCoinsWithMoreNegativeSentimentsThanPositive

from sentiment_analyzer.extraction import create_var, create_api, search_to_df, search_tweets
from sentiment_analyzer.cleaner import clean
from sentiment_analyzer.analyzer import analyzerOutput

from jobs.save import return_graph_view


from datetime import datetime, date
import calendar

# # Extraction
# import tweepy
# import pandas as pd
# consumer_key, consumer_key_secret, access_token, access_token_secret = create_var()
# def extract(consumer_key, consumer_key_secret, access_token, access_token_secret):
#     coin = ["Bitcoin","BNB","Ethereum","Tether","USD Coin","XRP"]
#     for x in range(0,len(coin)):
#         api = create_api(consumer_key, consumer_key_secret, access_token, access_token_secret)
#         search_results = search_tweets(api,coin[x], ignore_rt=True, max_tweets=400)
#         tweets = search_to_df(search_results)
#         tweets.to_csv("../sentiment_analyzer/out/" + coin[x] + ".csv", index=False)
#         # print("Extracting " + coin[x] + " tweets")

# t=datetime.now()
# if t.minute==46:
#     consumer_key, consumer_key_secret, access_token, access_token_secret = create_var()
#     print("yo")
#     extract(consumer_key, consumer_key_secret, access_token, access_token_secret)


# running analyzer output for all coins
btcAnalyzerOut = analyzerOutput("bitcoin")
ethAnalyzerOut = analyzerOutput("ethereum")
xrpAnalyzerOut = analyzerOutput("xrp")
usdcAnalyzerOut = analyzerOutput("usdcoin")
bnbAnalyzerOut = analyzerOutput("binance")
usdtAnalyzerOut = analyzerOutput("tether")

analyzerOutList = [btcAnalyzerOut, ethAnalyzerOut, xrpAnalyzerOut, usdcAnalyzerOut, bnbAnalyzerOut, usdtAnalyzerOut]


# 2 most recent values for each coin:
btcPrevVal = 21.5
ethPrevVal = 21.5
xrpPrevVal = 21.5
usdcPrevVal = 21.5
bnbPrevVal = 21.5
usdtPrevVal = 21.5

btcTwoVals = [btcPrevVal, round(btcAnalyzerOut[2], 2)]
ethTwoVals = [ethPrevVal, round(ethAnalyzerOut[2], 2)]
xrpTwoVals = [xrpPrevVal, round(xrpAnalyzerOut[2], 2)]
usdcTwoVals = [usdcPrevVal, round(usdcAnalyzerOut[2], 2)]
bnbTwoVals = [bnbPrevVal, round(bnbAnalyzerOut[2], 2)]
usdtTwoVals = [usdtPrevVal, round(usdtAnalyzerOut[2], 2)]

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

    context['bitcoin_comp_score'] = btcTwoVals[1]
    context['ethereum_comp_score'] = ethTwoVals[1]
    context['xrp_comp_score'] = xrpTwoVals[1]
    context['usd_comp_score'] = usdcTwoVals[1]
    context['bnb_comp_score'] = bnbTwoVals[1]
    context['tether_comp_score'] = usdtTwoVals[1]

    context['bitcoin_comp_score_fluc'] = getCompScoreFluctuation(btcTwoVals)
    context['ethereum_comp_score_fluc'] = getCompScoreFluctuation(ethTwoVals)
    context['xrp_comp_score_fluc'] = getCompScoreFluctuation(xrpTwoVals)
    context['usd_comp_score_fluc'] = getCompScoreFluctuation(usdcTwoVals)
    context['bnb_comp_score_fluc'] = getCompScoreFluctuation(bnbTwoVals)
    context['tether_comp_score_fluc'] = getCompScoreFluctuation(usdtTwoVals)

    context['bitcoin_comp_score_fluc_arrow'] = getCompScoreFluctuation(btcTwoVals) >= 0
    context['ethereum_comp_score_fluc_arrow'] = getCompScoreFluctuation(ethTwoVals) >= 0
    context['xrp_comp_score_fluc_arrow'] = getCompScoreFluctuation(xrpTwoVals) >= 0
    context['usd_comp_score_fluc_arrow'] = getCompScoreFluctuation(usdcTwoVals) >= 0
    context['bnb_comp_score_fluc_arrow'] = getCompScoreFluctuation(bnbTwoVals) >= 0
    context['tether_comp_score_fluc_arrow'] = getCompScoreFluctuation(usdtTwoVals) >= 0

    # for filter values
    context['positive_flucs'] = findPositiveAndNegativeFlucs(btcTwoVals, ethTwoVals, xrpTwoVals, usdcTwoVals, bnbTwoVals, usdtTwoVals)[0]
    context['negative_flucs'] = findPositiveAndNegativeFlucs(btcTwoVals, ethTwoVals, xrpTwoVals, usdcTwoVals, bnbTwoVals, usdtTwoVals)[1]
    context['max_positive_sentiment'] = analyzerOutList.index(max(analyzerOutList, key=lambda x: x[0]))
    context['min_positive_sentiment'] = analyzerOutList.index(min(analyzerOutList, key=lambda x: x[0]))
    context['max_negative_sentiment'] = analyzerOutList.index(max(analyzerOutList, key=lambda x: x[1]))
    context['min_negative_sentiment'] = analyzerOutList.index(min(analyzerOutList, key=lambda x: x[1]))
    context['more_positive_sentiments'] = getCoinsWithMorePositiveSentimentsThanNegative(analyzerOutList)
    context['more_negative_sentiments'] = getCoinsWithMoreNegativeSentimentsThanPositive(analyzerOutList)
    
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
    context['graph_folder'] = return_graph_view()

    return render(request, 'coin.html', context)

def reachview(request):
    context = {}
    return render(request, 'reach.html', context)