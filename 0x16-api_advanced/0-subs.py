#!/usr/bin/python3
"""
subscriber number module
"""
import requests


def number_of_subscribers(subreddit):
    """ returns subcsriber number """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'User'}

    response = requests.get(url, headers=header).json()
    subscribers = response['data']['subscribers']
    if subscribers:
        return subscribers
    return 0
