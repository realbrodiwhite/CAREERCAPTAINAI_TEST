# delete_tweet.py

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
    headers = {"Authorization": f"Bearer {bearer_token}"}
    return headers

def delete_tweet(headers, tweet_id):
    url = f"https://api.twitter.com/2/tweets/{tweet_id}"
    response = requests.delete(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Request returned an error: {response.status_code} {response.text}")
    return response.json()

if __name__ == "__main__":
    headers = create_headers(bearer_token)
    tweet_id = "your_tweet_id_here"
    delete_response = delete_tweet(headers, tweet_id)
    print(delete_response)
    with open('delete_response.json', 'w') as f:
        f.write(str(delete_response))
