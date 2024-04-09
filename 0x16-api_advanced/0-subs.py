#!/usr/bin/python3
"""
0-subs
"""
import requests


def number_of_subscribers(subreddit):
    """ a function that queries the Reddit API and returns the number
    of subscribers for a given subreddit """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    user_header = {'User-Agent': 'custom User-Agent'}

    response = requests.get(url, headers=user_header, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers_number = data['data']['subscribers']
        return subscribers_number
    else:
        return 0
