import warnings
from nltk.corpus import stopwords
import numpy as np
import pandas as pd
stopwords = stopwords.words('english')
warnings.filterwarnings('ignore')
import nltk
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
nltk.download('stopwords')
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


bitcoin = pd.read_csv('out/cleaned_Bitcoin.csv')
ethereum = pd.read_csv('out/cleaned_Ethereum.csv')
tether = pd.read_csv('out/cleaned_Tether.csv')
bnb = pd.read_csv('out/cleaned_BNB.csv')
usdc = pd.read_csv('out/cleaned_USD Coin.csv')
xrp = pd.read_csv('out/cleaned_XRP.csv')

def tweets_to_dtm(tweets,coin):
    vectorizer = CountVectorizer(max_features=2000)
    dtm = vectorizer.fit_transform(tweets)
    pickle.dump(vectorizer, open('out/' + coin +'_dtm.pk', 'wb'))
    return dtm, vectorizer

def tweets_to_ngram(tweets, coin,n=2):
    vectorizer = CountVectorizer(
        ngram_range=(n, n),
        token_pattern=r'\b\w+\b',
        min_df=1,
        max_features=2000)
    ngram = vectorizer.fit_transform(tweets)
    pickle.dump(vectorizer, open('out/'+ coin + '_ngram.pk', 'wb'))
    return ngram, vectorizer

def tweets_to_tfidf(tweets,coin):
    vectorizer = TfidfVectorizer(max_features=2000)
    tfidf = vectorizer.fit_transform(tweets)
    pickle.dump(vectorizer, open('out/' + coin + '_tfidf.pk', 'wb'))
    return tfidf, vectorizer

coins = [bitcoin,ethereum,tether,bnb,usdc,xrp]
coin_names = ["bitcoin","ethereum","tether","bnb","usdc","xrp"]
for x in range(0,len(coins)-1):
    tweets_to_dtm((coins[x]['cleaned_text']),coin_names[x])
    tweets_to_ngram(coins[x]['cleaned_text'],coin_names[x])
    tweets_to_tfidf(coins[x]['cleaned_text'],coin_names[x])
    print(type(coins[x]['cleaned_text']),x)

coins = [bitcoin,ethereum,tether,bnb,usdc,xrp]
coin_names = ["bitcoin","ethereum","tether","bnb","usdc","xrp"]

dtm_bitcoin, dtm_v_bitcoin = tweets_to_dtm(bitcoin['cleaned_text'],"bitcoin")
ngram_bitcoin, ngram_v_bitcoin = tweets_to_ngram(bitcoin['cleaned_text'],"bitcoin", n=2)
tfidf_bitcoin, tfidf_v_bitcoin = tweets_to_tfidf(bitcoin['cleaned_text'],"bitcoin")

dtm_ethereum, dtm_v_ethereum = tweets_to_dtm(ethereum['cleaned_text'],"ethereum")
ngram_ethereum, ngram_v_ethereum = tweets_to_ngram(ethereum['cleaned_text'],"ethereum", n=2)
tfidf_ethereum, tfidf_v_ethereum = tweets_to_tfidf(ethereum['cleaned_text'],"ethereum")

dtm_tether, dtm_v_tether = tweets_to_dtm(tether['cleaned_text'],"tether")
ngram_tether, ngram_v_tether = tweets_to_ngram(tether['cleaned_text'],"tether", n=2)
tfidf_tether, tfidf_v_tether = tweets_to_tfidf(tether['cleaned_text'],"tether")

dtm_bnb, dtm_v_bnb = tweets_to_dtm(bnb['cleaned_text'],"bnb")
ngram_bnb, ngram_v_bnb = tweets_to_ngram(bnb['cleaned_text'],"bnb", n=2)
tfidf_bnb, tfidf_v_bnb = tweets_to_tfidf(bnb['cleaned_text'],"bnb")

dtm_usdc, dtm_v_usdc = tweets_to_dtm(usdc['cleaned_text'],"usdc")
ngram_usdc, ngram_v_usdc = tweets_to_ngram(usdc['cleaned_text'],"usdc", n=2)
tfidf_usdc, tfidf_v_usdc = tweets_to_tfidf(usdc['cleaned_text'],"usdc")

def vector_to_frequency(vector, vectorizer):
    """
    Return a list of words and their corresponding occurence in the corpus
    """
    total = vector.sum(axis=0)
    frequency = [(w, total[0, i]) for w, i in vectorizer.vocabulary_.items()]
    frequency = pd.DataFrame(frequency, columns=['term', 'frequency'])
    frequency = frequency.sort_values(by='frequency', ascending=False).reset_index(drop=True)
    return frequency

coin_names = ["bitcoin","ethereum","tether","bnb","usdc","xrp"]

freq_dtm = vector_to_frequency(dtm_bitcoin, dtm_v_bitcoin)
freq_dtm.to_csv('out/bitcoin_dtm.csv', index=False)
freq_ngram = vector_to_frequency(ngram_bitcoin, ngram_v_bitcoin)
freq_ngram.to_csv('out/bitcoin_ngram.csv', index=False)
freq_tfidf = vector_to_frequency(tfidf_bitcoin, tfidf_v_bitcoin)
freq_tfidf.to_csv('out/bitcoin_tfidf.csv', index=False)

freq_dtm = vector_to_frequency(dtm_ethereum, dtm_v_ethereum)
freq_dtm.to_csv('out/ethereum_dtm.csv', index=False)
freq_ngram = vector_to_frequency(ngram_ethereum, ngram_v_ethereum)
freq_ngram.to_csv('out/ethereum_ngram.csv', index=False)
freq_tfidf = vector_to_frequency(tfidf_ethereum, tfidf_v_ethereum)
freq_tfidf.to_csv('out/ethereum_tfidf.csv', index=False)

freq_dtm = vector_to_frequency(dtm_tether, dtm_v_tether)
freq_dtm.to_csv('out/tether_dtm.csv', index=False)
freq_ngram = vector_to_frequency(ngram_tether, ngram_v_tether)
freq_ngram.to_csv('out/tether_ngram.csv', index=False)
freq_tfidf = vector_to_frequency(tfidf_tether, tfidf_v_tether)
freq_tfidf.to_csv('out/tether_tfidf.csv', index=False)

freq_dtm = vector_to_frequency(dtm_bnb, dtm_v_bnb)
freq_dtm.to_csv('out/bnb_dtm.csv', index=False)
freq_ngram = vector_to_frequency(ngram_bnb, ngram_v_bnb)
freq_ngram.to_csv('out/bnb_ngram.csv', index=False)
freq_tfidf = vector_to_frequency(tfidf_bnb, tfidf_v_bnb)
freq_tfidf.to_csv('out/bnb_tfidf.csv', index=False)

freq_dtm = vector_to_frequency(dtm_usdc, dtm_v_usdc)
freq_dtm.to_csv('out/usdc_dtm.csv', index=False)
freq_ngram = vector_to_frequency(ngram_usdc, ngram_v_usdc)
freq_ngram.to_csv('out/usdc_ngram.csv', index=False)
freq_tfidf = vector_to_frequency(tfidf_usdc, tfidf_v_usdc)
freq_tfidf.to_csv('out/usdc_tfidf.csv', index=False)