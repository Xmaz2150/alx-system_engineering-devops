#!/usr/bin/python3
"""
Gets users and todo list from {JSON} Placeholder API

Prints number of tasks user did
"""
import csv
import requests
import sys

if __name__ == '__main__':
    url_list = 'https://jsonplaceholder.typicode.com/todos?userId={}'
    url_users = 'https://jsonplaceholder.typicode.com/users/{}'

    user_id = sys.argv[1]
    todo_list = requests.get(url_list.format(user_id)).json()
    user = requests.get(url_users.format(user_id)).json()

    user_name = user.get('username')

    with open('{}.csv'.format(user_id), 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for item in todo_list:
            writer.writerow([
                user_id, user_name,
                item.get('completed'),
                item.get('title')
                ])
