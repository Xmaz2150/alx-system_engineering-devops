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
    url_list = 'https://jsonplaceholder.typicode.com/todos?userId={}'
    url_users = 'https://jsonplaceholder.typicode.com/users/{}'

    user_id = sys.argv[1]
    todo_list = requests.get(url_list.format(user_id)).json()
    user = requests.get(url_users.format(user_id)).json()

    user_name = user.get('username')

    user_tasks = []
    for item in todo_list:
        task_dict = {}
        task_dict['task'] = item.get('title')
        task_dict['completed'] = item.get('completed')
        task_dict['ussername'] = user_name
        user_tasks.append(task_dict)

    user_tasks_dict = {}
    user_tasks_dict[user_id] = user_tasks
    with open('{}.json'.format(user_id), 'w') as f:
        json.dump(user_tasks_dict, f)
