#!/usr/bin/python3
"""Number of subscribers."""
import json
import requests

def number_of_subscribers(subreddit):
    """takes a subreddit and returns the number of subscribers."""
    user_agent = {"User-Agent": "unix:0-subs.py:v1.0"}
    data = requests.get("https://www.reddit.com/r/{}/about.json"
                        .format(subreddit),
                        headers=user_agent,
                        allow_redirects=False)
    if data.status_code != 200:
        return 0
    json_data = data.json()
    results = json_data.get("data").get("subscribers")
    return results