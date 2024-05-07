#!/usr/bin/python3
"""
top 10 posts module
"""
import requests


def top_ten(subreddit):
    """ returns best posts of subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'User'}

    response = requests.get(url, headers=header).json()
    data = response['data']['children']

    s_data = sorted(data, key=lambda obj: obj['data']['score'], reverse=True)
    titles = [line['data']['title'] for line in s_data]

    for title in titles[:10]:
        print(title)
