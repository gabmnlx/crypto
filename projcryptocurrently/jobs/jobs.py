from django.conf import settings
import tweepy
import pandas as pd
from sentiment_analyzer.extraction import create_var, create_api, search_to_df, search_tweets
import json
from datetime import datetime

def schedule_extract():
    t=datetime.now()
    if t.minute==30 and t.second==00:
        print('NAG RUN')
        consumer_key, consumer_key_secret, access_token, access_token_secret = create_var()
        coin = ["Bitcoin","BNB","Ethereum","Tether","USD Coin","XRP"]
        for x in range(0,len(coin)):
            print("Extracting " + coin[x] + " tweets")
            api = create_api(consumer_key, consumer_key_secret, access_token, access_token_secret)
            search_results = search_tweets(api,coin[x], ignore_rt=True, max_tweets=400)
            tweets = search_to_df(search_results)
            tweets.to_csv("sentiment_analyzer/out/" + coin[x] + ".csv", index=False)
            print("Successfully extracted " + coin[x] + " tweets")
            