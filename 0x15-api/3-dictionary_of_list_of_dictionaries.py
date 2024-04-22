#!/usr/bin/python3
"""
Gets users and todo list from {JSON} Placeholder API

Prints number of tasks user did
"""
import csv
import json
import requests
import sys

if __name__ == '__main__':
    url_lists = 'https://jsonplaceholder.typicode.com/todos'
    url_users = 'https://jsonplaceholder.typicode.com/users'

    todo_lists = requests.get(url_lists).json()
    users = requests.get(url_users).json()

    def users_dict(user):
        user_tasks = []
        user_name = user.get('username')
        user_id = user.get('id')
        for item in todo_lists:
            if user_id == item.get('userId'):
                task_dict = {}
                task_dict['task'] = item.get('title')
                task_dict['completed'] = item.get('completed')
                task_dict['ussername'] = user_name
                user_tasks.append(task_dict)
        return user_tasks

    users_tasks_dicts = {}
    for user in users:
        users_tasks_dicts[user.get('id')] = users_dict(user)

    with open('{}.json'.format('todo_all_employees'), 'w') as f:
        json.dump(users_tasks_dicts, f)
