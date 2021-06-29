from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time 

import twitter_credentials

class listener(StreamListener):

    def on_data(self, data):
        try:
          saveFile = open('tweetDB.csv','a')
          saveFile.write(data)
          saveFile.write('\n')
          saveFile.close
          return True
        except BaseException:
          print('failed on tweet data')
          time.sleep(5)

    def on_error(self, status):
        print(status)


auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])
