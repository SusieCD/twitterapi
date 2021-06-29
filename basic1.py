from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time 
import json

import twitter_credentials

class listener(StreamListener):

    def on_data(self, data):
        try:
          all_data = json.loads(data)
          tweet = all_data["text"]
          username = all_data["user"]["screen_name"]
          trimed_data = username + " :: " + tweet
          saveFile = open('tweetDB2.csv','a')
          saveFile.write(trimed_data)
          saveFile.write('\n')
          saveFile.close
          print('5')
          return True
        except BaseException:
          print('failed on tweet data')
          time.sleep(5)

    def on_error(self, status):
        print(status)            
        if status == 429:
              print("App's rate limit having been exhausted for the resource. Waiting.....")
              time.sleep(15*60) # Waiting 15 minutes 


auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
print('1')
twitterStream = Stream(auth, listener())
print('2')
twitterStream.filter(track=["car"])
print('end')
