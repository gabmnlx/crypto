import nltk
# nltk.download('stopwords')
from turtle import clear
from nltk.corpus import stopwords
import numpy as np
import pandas as pd
from jobs.save import return_save
stopwords = stopwords.words('english')
# newStopWords = ["bitcoin","btc","ethereum","eth","tether","USD Coin","BNB","XRP"]
# stopwords.extend(newStopWords)

def clean_tweets(tweets):
    tweets['cleaned_text'] = tweets['text'].fillna('') # Remove blank texts
    tweets['cleaned_text'] = tweets['cleaned_text'].str.lower() # Transform into lowercase
    tweets['cleaned_text'] = tweets['cleaned_text'].str.replace(r'([^A-Za-z0-9_ \t])|(\w+:\/\/\S+)', '') # Remove non-alphanumeric characters
    tweets['cleaned_text'] = tweets['cleaned_text'].str.replace(r'^\s+|\s+$', '')  # Remove trailing and leading whitespaces
    tweets['cleaned_text'] = tweets['cleaned_text'].apply(lambda x: ' '.join([w for w in x.split() if w not in (stopwords)]))# Remove stopwords
    
    return tweets

def clean():
    save_destination = return_save()
    coin = ["Bitcoin","BNB","Ethereum","Tether","USD Coin","XRP"]
    for x in range(0,len(coin)):
        tw = pd.read_csv(save_destination + coin[x] + ".csv", index_col=None, header=0)
        cleaned = clean_tweets(tw)
        print("Cleaning " + coin[x] + " tweets")
        cleaned.to_csv(save_destination + "cleaned_" + coin[x] + ".csv", index=False)

