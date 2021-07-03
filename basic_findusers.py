
# import the module
import tweepy
from tweepy import OAuthHandler
import twitter_credentials

auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
 
  
# calling the api 
api = tweepy.API(auth)
  
# the query to be searched
q = "scott morrison"
  
# search the query
users = api.search_users(q)
  
# print the users retrieved
for user in users:
    print(user.screen_name)
