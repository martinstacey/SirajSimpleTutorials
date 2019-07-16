# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 13:53:45 2017

@author: Martin
"""
import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'YLBv24CrRWbbgvG1NFzhtDKAL'
consumer_secret= 'xUSlSDhgJ5AlIF0udFVyXmSHcESU6Y3Hgxt6ylASx0gvC5bsKr'

access_token='3394689994-bPG1eBUVUObtl1VlsGKVy5JUp1p9qMXRQ1yqD6A'
access_token_secret='VJdto5Nmjd4ZyLkHmVmodpwCEgluQK92KEwKLmi138kSB'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")