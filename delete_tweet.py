# delete_tweet.py

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

def delete_tweet(oauth, tweet_id):
    url = f"https://api.twitter.com/2/tweets/{tweet_id}"
    response = oauth.delete(url)
    if response.status_code != 200:
        raise Exception(f"Request returned an error: {response.status_code} {response.text}")
    return response.json()

if __name__ == "__main__":
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret, resource_owner_key=access_token, resource_owner_secret=access_token_secret)
    tweet_id = "1799950865618612334"  # Replace with the actual tweet ID
    delete_response = delete_tweet(oauth, tweet_id)
    print(delete_response)
    with open('delete_response.json', 'w') as f:
        f.write(str(delete_response))
