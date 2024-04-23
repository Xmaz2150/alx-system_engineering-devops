#!/usr/bin/python3
"""
Gets users and todo list from {JSON} Placeholder API

Prints number of tasks user did
"""
import requests
import sys

if __name__ == '__main__':
    userId = sys.argv[1]
    urlList = 'https://jsonplaceholder.typicode.com/todos?userId={}'
    urlUsers = 'https://jsonplaceholder.typicode.com/users/{}'

    todoList = requests.get(urlList.format(userId)).json()
    user = requests.get(urlUsers.format(userId)).json()

    doneTasks = [i.get('title') for i in todoList if i.get('completed')]
    userName = user.get('name')

    printStr = 'Employee {} is done with tasks({}/{}):'
    print(printStr.format(userName, len(doneTasks), len(todoList)))
    for task in doneTasks:
        print('\t{}'.format(task))
