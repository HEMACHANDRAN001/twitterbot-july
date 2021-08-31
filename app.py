# Final Code
import time
import tweepy
import os

consumer_key = os.getenv('consumer_key')
consumer_secret=os.getenv('consumer_secret')
access_token=os.getenv('access_token')
access_token_secret=os.getenv('access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
print("Authentication approved")
while True:
  user = api.get_user('@Ameen91741779')
  u = user.followers_count
  api.update_profile(name=f'AMEER {u} Followers')
  print(f'AMEER {u} Followers')
  time.sleep(60)
  
 
