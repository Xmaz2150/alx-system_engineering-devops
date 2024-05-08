#!/usr/bin/python3
"""
top 10 posts module
"""
import requests


def top_ten(subreddit):
    """ returns best posts of subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'User'}

    response = requests.get(url, headers=header, allow_redirects=False).json()
    data = response.get('data').get('children')

    if data:
        s_data = sorted(data, key=lambda obj: obj['data']['score'], reverse=True)
        titles = [line['data']['title'] for line in s_data]

        for title in titles[:10]:
            print(title)
    else:
        print(None)
