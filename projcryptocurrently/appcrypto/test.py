import tweepy
import pandas as pd
from datetime import datetime
def create_var():
    consumer_key = 'FvUZZRtXBHbuRFSfbrIxbVC2R'
    consumer_key_secret = 'QoNA68J1Ds9Jn3qYEmAAW3267suZ0Nq39JNe7dYzdUCaRwybfH'

    access_token = '1259565361-5k2vVN8qKjB1glxy2LlsofvXhQzoFTd9XCcKAWy'
    access_token_secret = 'Yeh7ctB0v0bqLq5uEi8QPdU9ubyo8n0Wnh1QFClDm3MAP'
    return consumer_key, consumer_key_secret, access_token, access_token_secret

def create_api(consumer_key, consumer_key_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

def search_tweets(api, query, ignore_rt=False, max_tweets=400, lang='en'):
    if ignore_rt:
        query = query + ' -filter:retweets'
    search = tweepy.Cursor(api.search_tweets, query, lang=lang, tweet_mode = "extended").items(max_tweets)
    return search

def search_to_df(search_results):
    tweets = [[t.id, t.user.screen_name,
               t.created_at, t.full_text]
              for t in search_results]
    tweets_df = pd.DataFrame(tweets, columns=['id', 'handle', 'created_at', 'text'])
    return tweets_df

def extract(consumer_key, consumer_key_secret, access_token, access_token_secret):
    coin = ["Bitcoin","BNB","Ethereum","Tether","USD Coin","XRP"]
    for x in range(0,len(coin)):
        api = create_api(consumer_key, consumer_key_secret, access_token, access_token_secret)
        search_results = search_tweets(api,coin[x], ignore_rt=True, max_tweets=400)
        tweets = search_to_df(search_results)
        tweets.to_csv("../sentiment_analyzer/out/" + coin[x] + ".csv", index=False)
        # print("Extracting " + coin[x] + " tweets")

t=datetime.now()
if t.minute==39:
    consumer_key, consumer_key_secret, access_token, access_token_secret = create_var()
    print("yo")
    extract(consumer_key, consumer_key_secret, access_token, access_token_secret)