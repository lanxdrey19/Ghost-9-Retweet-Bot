import tweepy
import time
import os
import dotenv
dotenv.load_dotenv(override=True)

consumer_key = str(os.getenv("CONSUMER_KEY"))
consumer_secret = str(os.getenv("CONSUMER_SECRET"))
access_token = str(os.getenv("ACCESS_TOKEN"))
access_token_secret = str(os.getenv("ACCESS_TOKEN_SECRET"))

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)



api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)



searchTerms = ["#고스트나인"]
nrTweets = 1

while True:

    for item in searchTerms:
        for tweet in tweepy.Cursor(api.search,item).items(nrTweets):
            try:
                tweet.favorite()
                tweet.retweet()
                time.sleep(60)
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break
        time.sleep(300)
