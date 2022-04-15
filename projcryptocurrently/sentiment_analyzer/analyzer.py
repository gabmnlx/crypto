from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

analyzer = SentimentIntensityAnalyzer()

def analyze(inputfile):
    analyze_results= []
    
    positive = 0
    pos_count = 0

    negative = 0
    neg_count = 0

    neutral = 0
    neu_count = 0

    compound = 0
    count = 0

    for line in inputfile:
        vs = analyzer.polarity_scores(line)
        if vs['compound'] > 0:
            pos_count += 1
            positive += vs['pos']
        elif vs['compound']  < 0:
            neg_count += 1
            negative += vs['neg']
        else:
            neu_count += 1
            neutral += vs['neu']
        count += 1
        compound += vs['compound']

    if neg_count == 0:
        neg_count+=1
    elif pos_count == 0:
        pos_count+=1

    ave_positive = positive/pos_count
    ave_negative = negative/neg_count
    ave_neutral = neutral/neu_count
    

    print("Positive: {}, Count: {}".format(ave_positive*100, pos_count))
    print("Negative: {}, Count: {}".format(ave_negative*100, neg_count))
    print("Compound Score: {}, Total Tweets: {}".format(compound/count*100,count))
    
    return [ave_positive*100,ave_negative*100,compound/count*100]

coins = ["cleaned_Bitcoin.csv","cleaned_BNB.csv","cleaned_Ethereum.csv","cleaned_Tether.csv","cleaned_USD Coin.csv"]
for x in coins:
    print(x.split('_')[1])
    y = pd.read_csv("out/" +x)
    analyze(y["cleaned_text"])
    print('\n')

