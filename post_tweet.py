# post_tweet.py

import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

bearer_token = os.getenv('BEARER_TOKEN')

# Verify that environment variables are loaded correctly
if not bearer_token:
    raise ValueError("BEARER_TOKEN environment variable is missing. Please check your .env file.")

def create_headers(bearer_token):
    headers = {"Authorization": f"Bearer {bearer_token}", "Content-Type": "application/json"}
    return headers

def post_tweet(headers, tweet_text):
    url = "https://api.twitter.com/2/tweets"
    payload = {"text": tweet_text}
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 201:
        raise Exception(f"Request returned an error: {response.status_code} {response.text}")
    return response.json()

if __name__ == "__main__":
    headers = create_headers(bearer_token)
    tweet_text = "Hello, this is a test tweet from CareerCaptain!"
    tweet_response = post_tweet(headers, tweet_text)
    print(tweet_response)
    with open('tweet_response.json', 'w') as f:
        f.write(str(tweet_response))
