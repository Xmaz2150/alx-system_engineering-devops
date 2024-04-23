#!/usr/bin/python3
"""
Gets users and todo list from {JSON} Placeholder API

Prints number of tasks user did
"""
import json
import requests

if __name__ == '__main__':
    urlLists = 'https://jsonplaceholder.typicode.com/todos'
    urlUsers = 'https://jsonplaceholder.typicode.com/users'

    todoLists = requests.get(urlLists).json()
    users = requests.get(urlUsers).json()

    def users_dict(user):
        userTasks = []
        userName = user.get('username')
        userId = user.get('id')
        for item in todoLists:
            if userId == item.get('userId'):
                taskDict = {}
                taskDict['task'] = item.get('title')
                taskDict['completed'] = item.get('completed')
                taskDict['ussername'] = userName
                userTasks.append(taskDict)
        return userTasks

    usersTasksDicts = {}
    for user in users:
        usersTasksDicts[user.get('id')] = users_dict(user)

    with open('{}.json'.format('todo_all_employees'), 'w') as f:
        json.dump(usersTasksDicts, f)
