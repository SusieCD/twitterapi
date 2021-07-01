#Twitter Search api for SYD area

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import time 
import json
import twitter_credentials

auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth,wait_on_rate_limit=True)


syd = '-33.8688,151.2093,10mi' 

for status in tweepy.Cursor(api.search,q = 'sydney', geocode = syd,tweet_mode="extended").items(260):
    jdata = json.dumps(status._json)
    all_data = json.loads(jdata)
    tweet = all_data["full_text"]
    saveFile = open('tweetDBsearch.csv','a')
    saveFile.write(tweet)
    saveFile.write('\n')
    saveFile.close


