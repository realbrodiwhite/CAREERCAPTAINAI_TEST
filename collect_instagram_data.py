# collect_instagram_data.py

import instaloader
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

instagram_username = os.getenv('INSTAGRAM_USERNAME')
instagram_password = os.getenv('INSTAGRAM_PASSWORD')

L = instaloader.Instaloader()

# Login (optional)
L.login(instagram_username, instagram_password)

# Get profile
profile = instaloader.Profile.from_username(L.context, instagram_username)

# Collect posts
posts_data = []
for post in profile.get_posts():
    posts_data.append({
        'date': post.date,
        'text': post.caption,
        'likes': post.likes,
        'comments': post.comments,
        'url': post.url
    })

# Save to JSON
with open('your_instagram_posts.json', 'w') as f:
    json.dump(posts_data, f)
