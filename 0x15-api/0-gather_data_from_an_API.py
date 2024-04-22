#!/usr/bin/python3
"""
Gets users and todo list from {JSON} Placeholder API

Prints number of tasks user did
"""
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]

    todo_list = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'.
            format(user_id)
            ).json()
    user = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.
            format(user_id)
            ).json()

    done_tasks = [i.get('title') for i in todo_list if i.get('completed')]
    user_name = user.get('name')

    print_str = 'Employee {} is done with tasks({}/{}):'
    print(print_str.format(user_name, len(done_tasks), len(todo_list)))
    for task in done_tasks:
        print('\t{}'.format(task))
