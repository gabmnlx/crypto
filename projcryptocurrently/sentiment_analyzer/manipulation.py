import warnings
from jobs.save import return_save
# from nltk.corpus import stopwords 
import numpy as np
import pandas as pd
# stopwords = stopwords.words('english')
warnings.filterwarnings('ignore')
import nltk
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# nltk.download('stopwords')
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

save_destination = return_save()

def tweets_to_dtm(tweets,coin):
    save_destination = return_save()
    vectorizer = CountVectorizer(max_features=2000)
    dtm = vectorizer.fit_transform(tweets)
    pickle.dump(vectorizer, open(save_destination + '' + coin +'_dtm.pk', 'wb'))
    return dtm, vectorizer

def tweets_to_ngram(tweets, coin,n=2):
    save_destination = return_save()
    vectorizer = CountVectorizer(
        ngram_range=(n, n),
        token_pattern=r'\b\w+\b',
        min_df=1,
        max_features=2000)
    ngram = vectorizer.fit_transform(tweets)
    pickle.dump(vectorizer, open(save_destination + ''+ coin + '_ngram.pk', 'wb'))
    return ngram, vectorizer

def tweets_to_tfidf(tweets,coin):
    save_destination = return_save()
    vectorizer = TfidfVectorizer(max_features=2000)
    tfidf = vectorizer.fit_transform(tweets)
    pickle.dump(vectorizer, open(save_destination + '' + coin + '_tfidf.pk', 'wb'))
    return tfidf, vectorizer

# coins = [bitcoin,ethereum,tether,bnb,usdc,xrp]
coin_names = ["bitcoin","ethereum","tether","bnb","usdc","xrp"]

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

def run():
    save_destination = return_save()
    print("Manipulating tweets")
    bitcoin = pd.read_csv(save_destination + 'cleaned_Bitcoin.csv')
    ethereum = pd.read_csv(save_destination + 'cleaned_Ethereum.csv')
    tether = pd.read_csv(save_destination + 'cleaned_Tether.csv')
    bnb = pd.read_csv(save_destination + 'cleaned_BNB.csv')
    usdc = pd.read_csv(save_destination + 'cleaned_USD Coin.csv')
    xrp = pd.read_csv(save_destination + 'cleaned_XRP.csv')

    coins = [bitcoin,ethereum,tether,bnb,usdc,xrp]
    coin_names = ["bitcoin","ethereum","tether","bnb","usdc","xrp"]
    for x in range(0,len(coins)):
        tweets_to_dtm((coins[x]['cleaned_text']),coin_names[x])
        tweets_to_ngram(coins[x]['cleaned_text'],coin_names[x])
        tweets_to_tfidf(coins[x]['cleaned_text'],coin_names[x])
        print(coin_names[x])

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

    dtm_xrp, dtm_v_xrp = tweets_to_dtm(xrp['cleaned_text'],"xrp")
    ngram_xrp, ngram_v_xrp = tweets_to_ngram(xrp['cleaned_text'],"xrp", n=2)
    tfidf_xrp, tfidf_v_xrp = tweets_to_tfidf(xrp['cleaned_text'],"xrp")


    freq_dtm = vector_to_frequency(dtm_bitcoin, dtm_v_bitcoin)
    freq_dtm.to_csv(save_destination + 'bitcoin_dtm.csv', index=False)
    freq_ngram = vector_to_frequency(ngram_bitcoin, ngram_v_bitcoin)
    freq_ngram.to_csv(save_destination + 'bitcoin_ngram.csv', index=False)
    freq_tfidf = vector_to_frequency(tfidf_bitcoin, tfidf_v_bitcoin)
    freq_tfidf.to_csv(save_destination + 'bitcoin_tfidf.csv', index=False)

    freq_dtm = vector_to_frequency(dtm_ethereum, dtm_v_ethereum)
    freq_dtm.to_csv(save_destination + 'ethereum_dtm.csv', index=False)
    freq_ngram = vector_to_frequency(ngram_ethereum, ngram_v_ethereum)
    freq_ngram.to_csv(save_destination + 'ethereum_ngram.csv', index=False)
    freq_tfidf = vector_to_frequency(tfidf_ethereum, tfidf_v_ethereum)
    freq_tfidf.to_csv(save_destination + 'ethereum_tfidf.csv', index=False)

    freq_dtm = vector_to_frequency(dtm_tether, dtm_v_tether)
    freq_dtm.to_csv(save_destination + 'tether_dtm.csv', index=False)
    freq_ngram = vector_to_frequency(ngram_tether, ngram_v_tether)
    freq_ngram.to_csv(save_destination + 'tether_ngram.csv', index=False)
    freq_tfidf = vector_to_frequency(tfidf_tether, tfidf_v_tether)
    freq_tfidf.to_csv(save_destination + 'tether_tfidf.csv', index=False)

    freq_dtm = vector_to_frequency(dtm_bnb, dtm_v_bnb)
    freq_dtm.to_csv(save_destination + 'bnb_dtm.csv', index=False)
    freq_ngram = vector_to_frequency(ngram_bnb, ngram_v_bnb)
    freq_ngram.to_csv(save_destination + 'bnb_ngram.csv', index=False)
    freq_tfidf = vector_to_frequency(tfidf_bnb, tfidf_v_bnb)
    freq_tfidf.to_csv(save_destination + 'bnb_tfidf.csv', index=False)

    freq_dtm = vector_to_frequency(dtm_usdc, dtm_v_usdc)
    freq_dtm.to_csv(save_destination + 'usdc_dtm.csv', index=False)
    freq_ngram = vector_to_frequency(ngram_usdc, ngram_v_usdc)
    freq_ngram.to_csv(save_destination + 'usdc_ngram.csv', index=False)
    freq_tfidf = vector_to_frequency(tfidf_usdc, tfidf_v_usdc)
    freq_tfidf.to_csv(save_destination + 'usdc_tfidf.csv', index=False)

    freq_dtm = vector_to_frequency(dtm_xrp, dtm_v_xrp)
    freq_dtm.to_csv(save_destination + 'xrp_dtm.csv', index=False)
    freq_ngram = vector_to_frequency(ngram_xrp, ngram_v_xrp)
    freq_ngram.to_csv(save_destination + 'xrp_ngram.csv', index=False)
    freq_tfidf = vector_to_frequency(tfidf_xrp, tfidf_v_xrp)
    freq_tfidf.to_csv(save_destination + 'xrp_tfidf.csv', index=False)