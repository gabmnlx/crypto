import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.style as style
# from wordcloud import WordCloud
style.use('fivethirtyeight')
sns.set(rc={'figure.figsize':(12,6)})

# Read cleaned tweets, term frequencies of DTM, ngram, and TFIDF
freq_dtm_bitcoin = pd.read_csv('out/bitcoin_dtm.csv', index_col=None, header=0)
freq_ngram_bitcoin = pd.read_csv('out/bitcoin_ngram.csv', index_col=None, header=0)
freq_tfidf_bitcoin = pd.read_csv('out/bitcoin_tfidf.csv', index_col=None, header=0)

freq_dtm_ethereum = pd.read_csv('out/ethereum_dtm.csv', index_col=None, header=0)
freq_ngram_ethereum = pd.read_csv('out/ethereum_ngram.csv', index_col=None, header=0)
freq_tfidf_ethereum = pd.read_csv('out/ethereum_tfidf.csv', index_col=None, header=0)

freq_dtm_bnb = pd.read_csv('out/bnb_dtm.csv', index_col=None, header=0)
freq_ngram_bnb = pd.read_csv('out/bnb_ngram.csv', index_col=None, header=0)
freq_tfidf_bnb = pd.read_csv('out/bnb_tfidf.csv', index_col=None, header=0)

freq_dtm_tether = pd.read_csv('out/tether_dtm.csv', index_col=None, header=0)
freq_ngram_tether = pd.read_csv('out/tether_ngram.csv', index_col=None, header=0)
freq_tfidf_tether = pd.read_csv('out/tether_tfidf.csv', index_col=None, header=0)

freq_dtm_usdc = pd.read_csv('out/usdc_dtm.csv', index_col=None, header=0)
freq_ngram_usdc = pd.read_csv('out/usdc_ngram.csv', index_col=None, header=0)
freq_tfidf_usdc = pd.read_csv('out/usdc_tfidf.csv', index_col=None, header=0)

freq_dtm_XRP = pd.read_csv('out/XRP_dtm.csv', index_col=None, header=0)
freq_ngram_XRP = pd.read_csv('out/XRP_ngram.csv', index_col=None, header=0)
freq_tfidf_XRP = pd.read_csv('out/XRP_tfidf.csv', index_col=None, header=0)
# cleaned_tweets = pd.read_csv('out/cleaned_Bitcoin.csv', index_col=None, header=0)
# cleaned_tweets.head()

def create_wordcloud(tweets,coin, max_words=500):
    """Create a wordcloud of most common words in a set of tweets"""
    
    # Transform text for WordCloud
    tweets = tweets['cleaned_text']
    tweets = tweets.dropna()
    tweets = ' '.join(tweets)
    tweets = tweets.replace(' ', ',')
    
    # Generate wordcloud image
    wc = WordCloud(background_color="white", max_words=max_words, colormap='plasma')
    wc.generate(tweets)
    plt.imshow(wc, interpolation='bilinear')
    plt.title('Twitter Generated Cloud', size=30)
    plt.axis("off")
    plt.savefig("graphs/" + coin +"_wordcloud.svg")


#bitcoin
sns.barplot(data=freq_dtm_bitcoin.head(10), x='term',
            y='frequency').set_title('Frequent terms in DTM')
plt.tight_layout()
plt.savefig("graphs/bitcoin_dtm.svg")

# Visualize frequencies
sns.barplot(data=freq_ngram_bitcoin.head(10), x='term',
            y='frequency').set_title('Frequent terms in Ngram')
plt.tight_layout()
plt.savefig("graphs/bitcoin_ngram.svg")

# Visualize frequencies
sns.barplot(data=freq_tfidf_bitcoin.head(10), x='term',
            y='frequency').set_title('Frequent terms in TFIDF')
plt.tight_layout()
plt.savefig("graphs/bitcoin_tfidf.svg")

bitcoin_cleaned = pd.read_csv('out/cleaned_Bitcoin.csv')
# create_wordcloud(bitcoin_cleaned,"bitcoin")


#ethereum
sns.barplot(data=freq_dtm_ethereum.head(10), x='term',
            y='frequency').set_title('Frequent terms in DTM')
plt.tight_layout()
plt.savefig("graphs/ethereum_dtm.svg")


sns.barplot(data=freq_ngram_ethereum.head(10), x='term',
            y='frequency').set_title('Frequent terms in Ngram')
plt.savefig("graphs/ethereum_ngram.svg")

sns.barplot(data=freq_tfidf_ethereum.head(10), x='term',
            y='frequency').set_title('Frequent terms in TFIDF')
plt.tight_layout()
plt.savefig("graphs/ethereum_tfidf.svg")

ethereum_cleaned = pd.read_csv('out/cleaned_Ethereum.csv')
# create_wordcloud(ethereum_cleaned,"ethereum")

#Tether
sns.barplot(data=freq_dtm_tether.head(10), x='term',
            y='frequency').set_title('Frequent terms in DTM')
plt.tight_layout()
plt.savefig("graphs/tether_dtm.svg")

sns.barplot(data=freq_ngram_tether.head(10), x='term',
            y='frequency').set_title('Frequent terms in Ngram')
plt.savefig("graphs/tether_ngram.svg")

sns.barplot(data=freq_tfidf_tether.head(10), x='term',
            y='frequency').set_title('Frequent terms in TFIDF')
plt.tight_layout()
plt.savefig("graphs/tether_tfidf.svg")

tether_cleaned = pd.read_csv('out/cleaned_Tether.csv')
# create_wordcloud(tether_cleaned,"tether")

#BNB
sns.barplot(data=freq_dtm_bnb.head(10), x='term',
            y='frequency').set_title('Frequent terms in DTM')
plt.tight_layout()
plt.savefig("graphs/bnb_dtm.svg")

sns.barplot(data=freq_ngram_bnb.head(10), x='term',
            y='frequency').set_title('Frequent terms in Ngram')
plt.savefig("graphs/bnb_ngram.svg")

sns.barplot(data=freq_tfidf_bnb.head(10), x='term',
            y='frequency').set_title('Frequent terms in TFIDF')
plt.tight_layout()
plt.savefig("graphs/bnb_tfidf.svg")

bnb_cleaned = pd.read_csv('out/cleaned_BNB.csv')
# create_wordcloud(bnb_cleaned,"BNB")

#USDC
sns.barplot(data=freq_dtm_usdc.head(10), x='term',
            y='frequency').set_title('Frequent terms in DTM')
plt.tight_layout()
plt.savefig("graphs/usdc_dtm.svg")

sns.barplot(data=freq_ngram_usdc.head(10), x='term',
            y='frequency').set_title('Frequent terms in Ngram')
plt.savefig("graphs/usdc_ngram.svg")

sns.barplot(data=freq_tfidf_usdc.head(10), x='term',
            y='frequency').set_title('Frequent terms in TFIDF')
plt.tight_layout()
plt.savefig("graphs/usdc_tfidf.svg")

usdc_cleaned = pd.read_csv('out/cleaned_USD Coin.csv')
# create_wordcloud(usdc_cleaned,"USDC")

#XRP
sns.barplot(data=freq_dtm_XRP.head(10), x='term',
            y='frequency').set_title('Frequent terms in DTM')
plt.tight_layout()
plt.savefig("graphs/XRP_dtm.svg")

sns.barplot(data=freq_ngram_XRP.head(10), x='term',
            y='frequency').set_title('Frequent terms in Ngram')
plt.savefig("graphs/XRP_ngram.svg")

sns.barplot(data=freq_tfidf_XRP.head(10), x='term',
            y='frequency').set_title('Frequent terms in TFIDF')
plt.tight_layout()
plt.savefig("graphs/XRP_tfidf.svg")

XRP_cleaned = pd.read_csv('out/cleaned_USD Coin.csv')
# create_wordcloud(XRP_cleaned,"XRP")