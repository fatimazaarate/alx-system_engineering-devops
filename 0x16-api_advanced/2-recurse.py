#!/usr/bin/python3
"""
0-subs
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ a function that queries the Reddit API and prints titles
    of hot posts """

    url = 'http://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    user_header = {'User-Agent': 'custom User-Agent'}

    response = requests.get(url, headers=user_header, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        if 'children' in data['data']:
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])

            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
