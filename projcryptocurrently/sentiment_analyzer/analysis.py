from multiprocessing.context import assert_spawning
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.style as style
from wordcloud import WordCloud
from jobs.save import return_save, return_graph_save
# style.use('fivethirtyeight')
# sns.set(rc={'figure.figsize':(12,6)})

save_destination = return_save()
graph_destination = return_graph_save()

# Read cleaned tweets, term frequencies of DTM, ngram, and TFIDF
# freq_dtm_bitcoin = pd.read_csv(save_destination + 'bitcoin_dtm.csv', index_col=None, header=0)
# freq_dtm_ethereum = pd.read_csv(save_destination + 'ethereum_dtm.csv', index_col=None, header=0)
# freq_dtm_bnb = pd.read_csv(save_destination + 'bnb_dtm.csv', index_col=None, header=0)
# freq_dtm_tether = pd.read_csv(save_destination + 'tether_dtm.csv', index_col=None, header=0)
# freq_dtm_usdc = pd.read_csv(save_destination + 'usdc_dtm.csv', index_col=None, header=0)
# freq_dtm_XRP = pd.read_csv(save_destination + 'XRP_dtm.csv', index_col=None, header=0)

# freq_ngram_bitcoin = pd.read_csv(save_destination + 'bitcoin_ngram.csv', index_col=None, header=0)
# freq_ngram_ethereum = pd.read_csv(save_destination + 'ethereum_ngram.csv', index_col=None, header=0)
# freq_ngram_bnb = pd.read_csv(save_destination + 'bnb_ngram.csv', index_col=None, header=0)
# freq_ngram_tether = pd.read_csv(save_destination + 'tether_ngram.csv', index_col=None, header=0)
# freq_ngram_usdc = pd.read_csv(save_destination + 'usdc_ngram.csv', index_col=None, header=0)
# freq_ngram_XRP = pd.read_csv(save_destination + 'XRP_ngram.csv', index_col=None, header=0)

# freq_tfidf_bitcoin = pd.read_csv(save_destination + 'bitcoin_tfidf.csv', index_col=None, header=0)
# freq_tfidf_ethereum = pd.read_csv(save_destination + 'ethereum_tfidf.csv', index_col=None, header=0)
# freq_tfidf_bnb = pd.read_csv(save_destination + 'bnb_tfidf.csv', index_col=None, header=0)
# freq_tfidf_tether = pd.read_csv(save_destination + 'tether_tfidf.csv', index_col=None, header=0)
# freq_tfidf_usdc = pd.read_csv(save_destination + 'usdc_tfidf.csv', index_col=None, header=0)
# freq_tfidf_XRP = pd.read_csv(save_destination + 'XRP_tfidf.csv', index_col=None, header=0)
# cleaned_tweets = pd.read_csv(save_destination + 'cleaned_Bitcoin.csv', index_col=None, header=0)
# cleaned_tweets.head()

def create_wordcloud(tweets,coin, max_words=500):
    graph_destination = return_graph_save()
    plt.figure(19)
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
    plt.savefig("../" + graph_destination + coin + "_wordcloud.svg")
    plt.clf()
    plt.close(19)


def dtm(coin):
    save_destination = return_save()
    graph_destination = return_graph_save()
    freq_dtm_bitcoin = pd.read_csv(save_destination + 'bitcoin_dtm.csv', index_col=None, header=0)
    freq_dtm_ethereum = pd.read_csv(save_destination + 'ethereum_dtm.csv', index_col=None, header=0)
    freq_dtm_bnb = pd.read_csv(save_destination + 'bnb_dtm.csv', index_col=None, header=0)
    freq_dtm_tether = pd.read_csv(save_destination + 'tether_dtm.csv', index_col=None, header=0)
    freq_dtm_usdc = pd.read_csv(save_destination + 'usdc_dtm.csv', index_col=None, header=0)
    freq_dtm_XRP = pd.read_csv(save_destination + 'XRP_dtm.csv', index_col=None, header=0)
    dtmGraph = None
    if coin=='bitcoin':
        plt.figure(1)
        dtmGraph = sns.barplot(x='term', y='frequency', orient='v', data=freq_dtm_bitcoin.head(10))
        for x in dtmGraph.get_xticklabels():
            x.set_rotation(30)
        dtmGraph.set_title('Frequent terms in DTM')
        plt.savefig("graphs/bitcoin_dtm.svg")
        plt.savefig("../" + graph_destination + "bitcoin_dtm.svg")
        plt.clf()
        plt.close(1)
    elif coin=='ethereum':
        plt.figure(2)
        dtmGraph = sns.barplot(x='term', y='frequency', orient='v', data=freq_dtm_ethereum.head(10))
        for x in dtmGraph.get_xticklabels():
            x.set_rotation(30)
        dtmGraph.set_title('Frequent terms in DTM')
        plt.savefig("graphs/ethereum_dtm.svg")
        plt.savefig("../" + graph_destination + "ethereum_dtm.svg")
        plt.clf()
        plt.close(2)
    elif coin=='tether':
        plt.figure(3)
        dtmGraph = sns.barplot(x='term', y='frequency', orient='v', data=freq_dtm_tether.head(10))
        for x in dtmGraph.get_xticklabels():
            x.set_rotation(30)
        dtmGraph.set_title('Frequent terms in DTM')
        plt.savefig("graphs/tether_dtm.svg")
        plt.savefig("../" + graph_destination + "tether_dtm.svg")
        plt.clf()
        plt.close(3)
    elif coin=='bnb':
        plt.figure(4)
        dtmGraph = sns.barplot(x='term', y='frequency', orient='v', data=freq_dtm_bnb.head(10))
        for x in dtmGraph.get_xticklabels():
            x.set_rotation(30)
        dtmGraph.set_title('Frequent terms in DTM')
        plt.savefig("graphs/bnb_dtm.svg")
        plt.savefig("../" + graph_destination + "bnb_dtm.svg")
        plt.clf()
        plt.close(4)
    elif coin=='usdc':
        plt.figure(5)
        dtmGraph = sns.barplot(x='term', y='frequency', orient='v', data=freq_dtm_usdc.head(10))
        for x in dtmGraph.get_xticklabels():
            x.set_rotation(30)
        dtmGraph.set_title('Frequent terms in DTM')
        plt.savefig("graphs/usdc_dtm.svg")
        plt.savefig("../" + graph_destination + "usdc_dtm.svg")
        plt.clf()
        plt.close(5)
    elif coin=='xrp':
        plt.figure(6)
        dtmGraph = sns.barplot(x='term', y='frequency', orient='v', data=freq_dtm_XRP.head(10))
        for x in dtmGraph.get_xticklabels():
            x.set_rotation(30)
        dtmGraph.set_title('Frequent terms in DTM')
        plt.savefig("graphs/XRP_dtm.svg")
        plt.savefig("../" + graph_destination + "XRP_dtm.svg")
        plt.clf()
        plt.close(6)
    return dtmGraph

def ngram(coin):
    save_destination = return_save()
    graph_destination = return_graph_save()
    freq_ngram_bitcoin = pd.read_csv(save_destination + 'bitcoin_ngram.csv', index_col=None, header=0)
    freq_ngram_ethereum = pd.read_csv(save_destination + 'ethereum_ngram.csv', index_col=None, header=0)
    freq_ngram_bnb = pd.read_csv(save_destination + 'bnb_ngram.csv', index_col=None, header=0)
    freq_ngram_tether = pd.read_csv(save_destination + 'tether_ngram.csv', index_col=None, header=0)
    freq_ngram_usdc = pd.read_csv(save_destination + 'usdc_ngram.csv', index_col=None, header=0)
    freq_ngram_XRP = pd.read_csv(save_destination + 'XRP_ngram.csv', index_col=None, header=0)
    ngramGraph = None
    if coin=='bitcoin':
        plt.figure(7)
        ngramGraph = sns.barplot(x='frequency', y='term', orient='h', data=freq_ngram_bitcoin.head(10))
        ngramGraph.set_title('Frequent terms in Ngram')
        plt.subplots_adjust(left=0.5)
        plt.savefig("graphs/bitcoin_ngram.svg")
        plt.savefig("../" + graph_destination + "bitcoin_ngram.svg")
        plt.clf()
        plt.close(7)
    elif coin=='ethereum':
        plt.figure(8)
        ngramGraph = sns.barplot(x='frequency', y='term', orient='h', data=freq_ngram_ethereum.head(10))
        ngramGraph.set_title('Frequent terms in Ngram')
        plt.subplots_adjust(left=0.5)
        plt.savefig("graphs/ethereum_ngram.svg")
        plt.savefig("../" + graph_destination + "ethereum_ngram.svg")
        plt.clf()
        plt.close(8)
    elif coin=='tether':
        plt.figure(9)
        ngramGraph = sns.barplot(x='frequency', y='term', orient='h', data=freq_ngram_tether.head(10))
        ngramGraph.set_title('Frequent terms in Ngram')
        plt.subplots_adjust(left=0.5)
        plt.savefig("graphs/tether_ngram.svg")
        plt.savefig("../" + graph_destination + "tether_ngram.svg")
        plt.clf()
        plt.close(9)
    elif coin=='bnb':
        plt.figure(10)
        ngramGraph = sns.barplot(x='frequency', y='term', orient='h', data=freq_ngram_bnb.head(10))
        ngramGraph.set_title('Frequent terms in Ngram')
        plt.subplots_adjust(left=0.5)
        plt.savefig("graphs/bnb_ngram.svg")
        plt.savefig("../" + graph_destination + "bnb_ngram.svg")
        plt.clf()
        plt.close(10)
    elif coin=='usdc':
        plt.figure(11)
        ngramGraph = sns.barplot(x='frequency', y='term', orient='h', data=freq_ngram_usdc.head(10))
        ngramGraph.set_title('Frequent terms in Ngram')
        plt.subplots_adjust(left=0.5)
        plt.savefig("graphs/usdc_ngram.svg")
        plt.savefig("../" + graph_destination + "usdc_ngram.svg")
        plt.clf()
        plt.close(11)
    elif coin=='xrp':
        plt.figure(12)
        ngramGraph = sns.barplot(x='frequency', y='term', orient='h', data=freq_ngram_XRP.head(10))
        ngramGraph.set_title('Frequent terms in Ngram')
        plt.subplots_adjust(left=0.5)
        plt.savefig("graphs/XRP_ngram.svg")
        plt.savefig("../" + graph_destination + "XRP_ngram.svg")
        plt.clf()
        plt.close(12)
    return ngramGraph

def tfidf(coin):
    save_destination = return_save()
    graph_destination = return_graph_save()
    freq_tfidf_bitcoin = pd.read_csv(save_destination + 'bitcoin_tfidf.csv', index_col=None, header=0)
    freq_tfidf_ethereum = pd.read_csv(save_destination + 'ethereum_tfidf.csv', index_col=None, header=0)
    freq_tfidf_bnb = pd.read_csv(save_destination + 'bnb_tfidf.csv', index_col=None, header=0)
    freq_tfidf_tether = pd.read_csv(save_destination + 'tether_tfidf.csv', index_col=None, header=0)
    freq_tfidf_usdc = pd.read_csv(save_destination + 'usdc_tfidf.csv', index_col=None, header=0)
    freq_tfidf_XRP = pd.read_csv(save_destination + 'XRP_tfidf.csv', index_col=None, header=0)
    tfidfGraph = None
    if coin=='bitcoin':
        plt.figure(13)
        tfidfGraph = sns.barplot(x='term', y='frequency', orient='v', data=freq_tfidf_bitcoin.head(10))
        for x in tfidfGraph.get_xticklabels():
            x.set_rotation(30)
        tfidfGraph.set_title('Frequent terms in TFIDF')
        plt.savefig("graphs/bitcoin_tfidf.svg")
        plt.savefig("../" + graph_destination + "bitcoin_tfidf.svg")
        plt.clf()
        plt.close(13)
    elif coin=='ethereum':
        plt.figure(14)
        tfidfGraph = sns.barplot(x='term', y='frequency', orient='v', data=freq_tfidf_ethereum.head(10))
        for x in tfidfGraph.get_xticklabels():
            x.set_rotation(30)
        tfidfGraph.set_title('Frequent terms in TFIDF')
        plt.savefig("graphs/ethereum_tfidf.svg")
        plt.savefig("../" + graph_destination + "ethereum_tfidf.svg")
        plt.clf()
        plt.close(14)
    elif coin=='tether':
        plt.figure(15)
        tfidfGraph = sns.barplot(x='term', y='frequency', orient='v', data=freq_tfidf_tether.head(10))
        for x in tfidfGraph.get_xticklabels():
            x.set_rotation(30)
        tfidfGraph.set_title('Frequent terms in TFIDF')
        plt.savefig("graphs/tether_tfidf.svg")
        plt.savefig("../" + graph_destination + "tether_tfidf.svg")
        plt.clf()
        plt.close(15)
    elif coin=='bnb':
        plt.figure(16)
        tfidfGraph = sns.barplot(x='term', y='frequency', orient='v', data=freq_tfidf_bnb.head(10))
        for x in tfidfGraph.get_xticklabels():
            x.set_rotation(30)
        tfidfGraph.set_title('Frequent terms in TFIDF')
        plt.savefig("graphs/bnb_tfidf.svg")
        plt.savefig("../" + graph_destination + "bnb_tfidf.svg")
        plt.clf()
        plt.close(16)
    elif coin=='usdc':
        plt.figure(17)
        tfidfGraph = sns.barplot(x='term', y='frequency', orient='v', data=freq_tfidf_usdc.head(10))
        for x in tfidfGraph.get_xticklabels():
            x.set_rotation(30)
        tfidfGraph.set_title('Frequent terms in TFIDF')
        plt.savefig("graphs/usdc_tfidf.svg")
        plt.savefig("../" + graph_destination + "usdc_tfidf.svg")
        plt.clf()
        plt.close(17)
    elif coin=='xrp':
        plt.figure(18)
        tfidfGraph = sns.barplot(x='term', y='frequency', orient='v', data=freq_tfidf_XRP.head(10))
        for x in tfidfGraph.get_xticklabels():
            x.set_rotation(30)
        tfidfGraph.set_title('Frequent terms in TFIDF')
        plt.savefig("graphs/XRP_tfidf.svg")
        plt.savefig("../" + graph_destination + "XRP_tfidf.svg")
        plt.clf()
        plt.close(18)
    return tfidfGraph

def run_analysis():
    print("Running analysis")
    coins = ['bitcoin', 'ethereum', 'tether', 'bnb', 'usdc', 'xrp']
    plt.tight_layout()
    for coin in coins:
        dtm(coin)
        tfidf(coin)
        ngram(coin)
        if coin=='bitcoin':
            bitcoin_cleaned = pd.read_csv(save_destination + 'cleaned_Bitcoin.csv')
            create_wordcloud(bitcoin_cleaned,"bitcoin")
        elif coin=='ethereum':
            ethereum_cleaned = pd.read_csv(save_destination + 'cleaned_Ethereum.csv')
            create_wordcloud(ethereum_cleaned,"ethereum")
        elif coin=='tether':
            tether_cleaned = pd.read_csv(save_destination + 'cleaned_Tether.csv')
            create_wordcloud(tether_cleaned,"tether")
        elif coin=='bnb':
            bnb_cleaned = pd.read_csv(save_destination + 'cleaned_BNB.csv')
            create_wordcloud(bnb_cleaned,"BNB")
        elif coin=='usdc':
            usdc_cleaned = pd.read_csv(save_destination + 'cleaned_USD Coin.csv')
            create_wordcloud(usdc_cleaned,"USDC")
        elif coin=='xrp':
            XRP_cleaned = pd.read_csv(save_destination + 'cleaned_USD Coin.csv')
            create_wordcloud(XRP_cleaned,"XRP")


# #bitcoin
# coinGraph = sns.barplot(data=freq_dtm_bitcoin.head(10), x='term',
#             y='frequency')
# for x in coinGraph.get_xticklabels():
#     x.set_rotation(45)
# coinGraph.set_title('Frequent terms in DTM')
# plt.tight_layout()
# plt.savefig("graphs/bitcoin_dtm.svg")
# plt.savefig("../" + graph_destination + "bitcoin_dtm.svg") #for loading the image in the coin details kasi nag-eerror pag kinkukha sa sentiment_analyzer

# # Visualize frequencies
# coinGraph = sns.barplot(data=freq_ngram_bitcoin.head(10), x='term',
#             y='frequency')
# for x in coinGraph.get_xticklabels():
#     x.set_rotation(90)
# coinGraph.set_title('Frequent terms in Ngram')
# plt.tight_layout()
# plt.savefig("graphs/bitcoin_ngram.svg")
# plt.savefig("../" + graph_destination + "bitcoin_ngram.svg")

# # Visualize frequencies
# coinGraph = sns.barplot(data=freq_tfidf_bitcoin.head(10), x='term',
#             y='frequency')
# for x in coinGraph.get_xticklabels():
#     x.set_rotation(45)
# coinGraph.set_title('Frequent terms in TFIDF')
# plt.tight_layout()
# plt.savefig("graphs/bitcoin_tfidf.svg")
# plt.savefig("../" + graph_destination + "bitcoin_tfidf.svg")

# bitcoin_cleaned = pd.read_csv(save_destination + 'cleaned_Bitcoin.csv')
# create_wordcloud(bitcoin_cleaned,"bitcoin")


# #ethereum
# coinGraph = sns.barplot(data=freq_dtm_ethereum.head(10), x='term',
#             y='frequency')
# for x in coinGraph.get_xticklabels():
#     x.set_rotation(45)
# coinGraph.set_title('Frequent terms in DTM')
# plt.tight_layout()
# plt.savefig("graphs/ethereum_dtm.svg")
# plt.savefig("../" + graph_destination + "ethereum_dtm.svg")


# coinGraph = sns.barplot(data=freq_ngram_ethereum.head(10), x='term',
#             y='frequency')
# for x in coinGraph.get_xticklabels():
#     x.set_rotation(45)
# coinGraph.set_title('Frequent terms in Ngram')
# plt.savefig("graphs/ethereum_ngram.svg")
# plt.savefig("../" + graph_destination + "ethereum_ngram.svg")

# coinGraph = sns.barplot(data=freq_tfidf_ethereum.head(10), x='term',
#             y='frequency')
# for x in coinGraph.get_xticklabels():
#     x.set_rotation(45)
# coinGraph.set_title('Frequent terms in TFIDF')
# plt.tight_layout()
# plt.savefig("graphs/ethereum_tfidf.svg")
# plt.savefig("../" + graph_destination + "ethereum_tfidf.svg")

# ethereum_cleaned = pd.read_csv(save_destination + 'cleaned_Ethereum.csv')
# create_wordcloud(ethereum_cleaned,"ethereum")

# #Tether
# coinGraph = sns.barplot(data=freq_dtm_tether.head(10), x='term',
#             y='frequency')
# for x in coinGraph.get_xticklabels():
#     x.set_rotation(45)
# coinGraph.set_title('Frequent terms in DTM')
# plt.tight_layout()
# plt.savefig("graphs/tether_dtm.svg")
# plt.savefig("../" + graph_destination + "tether_dtm.svg")

# coinGraph = sns.barplot(data=freq_ngram_tether.head(10), x='term',
#             y='frequency')
# for x in coinGraph.get_xticklabels():
#     x.set_rotation(45)
# coinGraph.set_title('Frequent terms in Ngram')
# plt.savefig("graphs/tether_ngram.svg")
# plt.savefig("../" + graph_destination + "tether_ngram.svg")

# coinGraph = sns.barplot(data=freq_tfidf_tether.head(10), x='term',
#             y='frequency')
# for x in coinGraph.get_xticklabels():
#     x.set_rotation(45)
# coinGraph.set_title('Frequent terms in TFIDF')
# plt.tight_layout()
# plt.savefig("graphs/tether_tfidf.svg")
# plt.savefig("../" + graph_destination + "tether_tfidf.svg")

# tether_cleaned = pd.read_csv(save_destination + 'cleaned_Tether.csv')
# create_wordcloud(tether_cleaned,"tether")

# #BNB
# coinGraph = sns.barplot(data=freq_dtm_bnb.head(10), x='term',
#             y='frequency')
# for x in coinGraph.get_xticklabels():
#     x.set_rotation(45)
# coinGraph.set_title('Frequent terms in DTM')
# plt.tight_layout()
# plt.savefig("graphs/bnb_dtm.svg")
# plt.savefig("../" + graph_destination + "bnb_dtm.svg")

# coinGraph = sns.barplot(data=freq_ngram_bnb.head(10), x='term',
#             y='frequency')
# for x in coinGraph.get_xticklabels():
#     x.set_rotation(45)
# coinGraph.set_title('Frequent terms in Ngram')
# plt.savefig("graphs/bnb_ngram.svg")
# plt.savefig("../" + graph_destination + "bnb_ngram.svg")

# coinGraph = sns.barplot(data=freq_tfidf_bnb.head(10), x='term',
#             y='frequency')
# for x in coinGraph.get_xticklabels():
#     x.set_rotation(45)
# coinGraph.set_title('Frequent terms in TFIDF')
# plt.tight_layout()
# plt.savefig("graphs/bnb_tfidf.svg")
# plt.savefig("../" + graph_destination + "bnb_tfidf.svg")

# bnb_cleaned = pd.read_csv(save_destination + 'cleaned_BNB.csv')
# create_wordcloud(bnb_cleaned,"BNB")

# #USDC
# coinGraph = sns.barplot(data=freq_dtm_usdc.head(10), x='term',
#             y='frequency')
# for x in coinGraph.get_xticklabels():
#     x.set_rotation(45)
# coinGraph.set_title('Frequent terms in DTM')
# plt.tight_layout()
# plt.savefig("graphs/usdc_dtm.svg")
# plt.savefig("../" + graph_destination + "usdc_dtm.svg")

# coinGraph = sns.barplot(data=freq_ngram_usdc.head(10), x='term',
#             y='frequency')
# for x in coinGraph.get_xticklabels():
#     x.set_rotation(45)
# coinGraph.set_title('Frequent terms in Ngram')
# plt.savefig("graphs/usdc_ngram.svg")
# plt.savefig("../" + graph_destination + "usdc_ngram.svg")

# coinGraph = sns.barplot(data=freq_tfidf_usdc.head(10), x='term',
#             y='frequency')
# for x in coinGraph.get_xticklabels():
#     x.set_rotation(45)
# coinGraph.set_title('Frequent terms in TFIDF')
# plt.tight_layout()
# plt.savefig("graphs/usdc_tfidf.svg")
# plt.savefig("../" + graph_destination + "usdc_tfidf.svg")

# usdc_cleaned = pd.read_csv(save_destination + 'cleaned_USD Coin.csv')
# create_wordcloud(usdc_cleaned,"USDC")

# #XRP
# coinGraph = sns.barplot(data=freq_dtm_XRP.head(10), x='term',
#             y='frequency')
# for x in coinGraph.get_xticklabels():
#     x.set_rotation(45)
# coinGraph.set_title('Frequent terms in DTM')
# plt.tight_layout()
# plt.savefig("graphs/XRP_dtm.svg")
# plt.savefig("../" + graph_destination + "XRP_dtm.svg")

# coinGraph = sns.barplot(data=freq_ngram_XRP.head(10), x='term',
#             y='frequency')
# for x in coinGraph.get_xticklabels():
#     x.set_rotation(45)
# coinGraph.set_title('Frequent terms in Ngram')
# plt.savefig("graphs/XRP_ngram.svg")
# plt.savefig("../" + graph_destination + "XRP_ngram.svg")

# coinGraph = sns.barplot(data=freq_tfidf_XRP.head(10), x='term',
#             y='frequency')
# for x in coinGraph.get_xticklabels():
#     x.set_rotation(45)
# coinGraph.set_title('Frequent terms in TFIDF')
# plt.tight_layout()
# plt.savefig("graphs/XRP_tfidf.svg")
# plt.savefig("../" + graph_destination + "XRP_tfidf.svg")

# XRP_cleaned = pd.read_csv(save_destination + 'cleaned_USD Coin.csv')
# create_wordcloud(XRP_cleaned,"XRP")