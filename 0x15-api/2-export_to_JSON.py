#!/usr/bin/python3
"""
Gets users and todo list from {JSON} Placeholder API

Prints number of tasks user did
"""
import json
import requests
import sys

if __name__ == '__main__':
    urlList = 'https://jsonplaceholder.typicode.com/todos?userId={}'
    urlUsers = 'https://jsonplaceholder.typicode.com/users/{}'

    userId = sys.argv[1]
    todoList = requests.get(urlList.format(userId)).json()
    user = requests.get(urlUsers.format(userId)).json()

    userName = user.get('username')

    userTasks = []
    for item in todoList:
        taskDict = {}
        taskDict['task'] = item.get('title')
        taskDict['completed'] = item.get('completed')
        taskDict['ussername'] = userName
        userTasks.append(taskDict)

    userTasksDict = {}
    userTasksDict[userId] = userTasks
    with open('{}.json'.format(userId), 'w') as f:
        json.dump(userTasksDict, f)
