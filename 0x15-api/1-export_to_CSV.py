#!/usr/bin/python3
"""
Gets users and todo list from {JSON} Placeholder API

Prints number of tasks user did
"""
import csv
import requests
import sys

if __name__ == '__main__':
    urlList = 'https://jsonplaceholder.typicode.com/todos?userId={}'
    urlUsers = 'https://jsonplaceholder.typicode.com/users/{}'

    userId = sys.argv[1]
    todoList = requests.get(urlList.format(userId)).json()
    user = requests.get(urlUsers.format(userId)).json()

    userName = user.get('username')

    with open('{}.csv'.format(userId), 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for item in todoList:
            writer.writerow([
                userId, userName,
                item.get('completed'),
                item.get('title')
                ])
