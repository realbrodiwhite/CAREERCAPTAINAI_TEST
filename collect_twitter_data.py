# collect_twitter_data.py

import tweepy
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env filej
load_dotenv()

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
twitter_handle = os.getenv('TWITTER_HANDLE')

# Verify that environment variables are loaded correctly
if not all([consumer_key, consumer_secret, access_token, access_token_secret, twitter_handle]):
    raise ValueError("One or more environment variables are missing. Please check your .env file.")

# Set up Tweepy with your credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

try:
    # Collect tweets from your timeline
    tweets = api.user_timeline(screen_name=twitter_handle.strip('@'), count=200, tweet_mode='extended')

    # Process and store tweets
    tweets_data = []
    for tweet in tweets:
        tweets_data.append({
            'date': tweet.created_at,
            'text': tweet.full_text,
            'likes': tweet.favorite_count,
            'retweets': tweet.retweet_count,
            'comments': tweet.reply_count
        })

    # Save to JSON
    with open('your_tweets.json', 'w') as f:
        json.dump(tweets_data, f)

    print("Tweets collected successfully and saved to your_tweets.json.")

except tweepy.TweepError as e:
    print(f"Error: {e.reason}")
