# post_tweet.py

import requests
import os
from requests_oauthlib import OAuth1Session
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

# Verify that environment variables are loaded correctly
if not all([consumer_key, consumer_secret, access_token, access_token_secret]):
    raise ValueError("One or more environment variables are missing. Please check your .env file.")

def create_headers(oauth):
    headers = {"Authorization": f"Bearer {oauth.token}"}
    return headers

def post_tweet(oauth, tweet_text):
    url = "https://api.twitter.com/2/tweets"
    payload = {"text": tweet_text}
    response = oauth.post(url, json=payload)
    if response.status_code != 201:
        raise Exception(f"Request returned an error: {response.status_code} {response.text}")
    return response.json()

if __name__ == "__main__":
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret, resource_owner_key=access_token, resource_owner_secret=access_token_secret)
    tweet_text = "Hello, this is a test tweet from CareerCaptain!"
    tweet_response = post_tweet(oauth, tweet_text)
    print(tweet_response)
    with open('tweet_response.json', 'w') as f:
        f.write(str(tweet_response))
