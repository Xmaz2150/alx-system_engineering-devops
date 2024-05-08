#!/usr/bin/python3
"""
subscriber number module
"""
import requests


def number_of_subscribers(subreddit):
    """ returns subcsriber number """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'User'}

    response = requests.get(url, headers=header, allow_redirects=False).json()
    subscribers = response.get('data').get('subscribers')
    if subscribers:
        return subscribers
    return 0
