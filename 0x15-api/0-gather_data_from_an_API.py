#!/usr/bin/python3
"""
Gets users and todo list from {JSON} Placeholder API

Prints number of tasks user did
"""
import requests
import sys

if __name__ == '__main__':
    url_list = 'https://jsonplaceholder.typicode.com/todos'
    url_users = 'https://jsonplaceholder.typicode.com/users'

    user_id = sys.argv[1]
    response_list = requests.get(url_list)
    response_users = requests.get(url_users)

    todo_list = response_list.json()
    users_list = response_users.json()

    users_todo_list = [i for i in todo_list if i['userId'] == int(user_id)]
    done_tasks = [i for i in users_todo_list if i['completed']]
    user = [i for i in users_list if i['id'] == int(user_id)]
    user_name = user[0]['name']

    print_str = 'Employee {} is done with tasks({}/{}):'
    print(print_str.format(user_name, len(done_tasks), len(users_todo_list)))
    for task in done_tasks:
        print('\t{}'.format(task['title']))
