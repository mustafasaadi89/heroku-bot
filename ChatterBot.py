# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "CNxglqCtUkgfIgZBUe5g7yIOn"
consumer_secret = "4wcjWueKMzIMobugMQW50nsKs3dD87NIAbQr9482euCrd3JE53"
access_token = "858735119514845184-IIsQs9jsd3JeWDHKRxpp6CvCq8NoolJ"
access_token_secret = "l4Q2JkvIk0ub7wxzrHg08Z1K1sJxgiH6WPYi1uYglL8vH"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERE