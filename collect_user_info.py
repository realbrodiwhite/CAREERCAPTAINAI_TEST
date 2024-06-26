# collect_user_info.py

import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

bearer_token = os.getenv('BEARER_TOKEN')
twitter_handle = os.getenv('TWITTER_HANDLE')

# Verify that environment variables are loaded correctly
if not all([bearer_token, twitter_handle]):
    raise ValueError("One or more environment variables are missing. Please check your .env file.")

def create_headers(bearer_token):
    headers = {"Authorization": f"Bearer {bearer_token}"}
    return headers

def get_user_info(headers, twitter_handle):
    url = f"https://api.twitter.com/2/users/by/username/{twitter_handle}"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Request returned an error: {response.status_code} {response.text}")
    return response.json()

if __name__ == "__main__":
    headers = create_headers(bearer_token)
    user_info = get_user_info(headers, twitter_handle.strip('@'))
    print(user_info)
    with open('user_info.json', 'w') as f:
        f.write(str(user_info))
