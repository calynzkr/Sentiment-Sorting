#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nltk 
import nltk.data
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


import pandas as pd


senti = pd.read_csv("/Users/calyn/Documents/Fall 2020/595/Sentiment Sorting/mergedresult.csv")

analyser = SentimentIntensityAnalyzer()

def sent(text):
        score  = analyser.polarity_scores(text)
        score1 = score["compound"]
        return score1


def Purpose(data):
    purpose = list(senti.iloc[:,1])
    sentiment = list(map(sent,purpose))
    senti['Sentiment_Score'] = sentiment
    senti.sort_values(by=['Sentiment_Score'], inplace=True, ascending=False)
    return senti

senti = Purpose(senti)
top_10 = senti.nlargest(10,['Sentiment_Score'])
top_10.to_csv("Best 10.csv",index=False)
last_10 = senti.nsmallest(10,['Sentiment_Score'])
last_10.to_csv("Last 10.csv",index=False)

