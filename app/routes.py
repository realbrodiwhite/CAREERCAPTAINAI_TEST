# routes.py

from flask import render_template, request, redirect, url_for, flash
from app import app
from get_user_info import get_user_info
from post_tweet import post_tweet
from delete_tweet import delete_tweet

@app.route('/')
def index():
    try:
        user_info = get_user_info()
        user_name = user_info['data']['name']
        user_username = user_info['data']['username']
    except Exception as e:
        user_name = "Unknown"
        user_username = "Unknown"
        flash(f"An error occurred while fetching user info: {str(e)}", 'danger')
    return render_template('index.html', user_name=user_name, user_username=user_username)

@app.route('/post_tweet', methods=['POST'])
def post_tweet_route():
    if request.method == 'POST':
        tweet_text = request.form['tweet_text']
        try:
            response = post_tweet(tweet_text)
            flash(f"Tweet posted successfully: {response['data']['text']}", 'success')
        except Exception as e:
            flash(f"An error occurred while posting the tweet: {str(e)}", 'danger')
        return redirect(url_for('index'))

@app.route('/delete_tweet', methods=['POST'])
def delete_tweet_route():
    if request.method == 'POST':
        tweet_id = request.form['tweet_id']
        try:
            response = delete_tweet(tweet_id)
            flash(f"Tweet deleted successfully", 'success')
        except Exception as e:
            flash(f"An error occurred while deleting the tweet: {str(e)}", 'danger')
        return redirect(url_for('index'))
