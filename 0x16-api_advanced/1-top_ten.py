#!/usr/bin/python3
"""
1-top_ten.py
"""
import requests


def top_ten(subreddit):
    """a function that queries the Reddit API and prints the
    titles of the first 10 hot posts listed for a given subreddit."""

    url = f"https://www.reddit.com/r/{subreddit}//hot.json"
    user_header = {'User-Agent': 'custom User-Agent'}

    response = requests.get(url, headers=user_header, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for i, post in enumerate(posts[:10], 1):
            print(f"{post['data']['title']}")
    else:
        print("None")
