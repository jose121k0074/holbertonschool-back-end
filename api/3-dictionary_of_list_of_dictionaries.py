#!/usr/bin/python3
"""given employee ID returns all his todo list"""


import json
import requests
import sys


if __name__ == "__main__":
    names = requests.get('https://jsonplaceholder.typicode.com/users')
    json_names = names.json()

    general_dict = {}

    for user in json_names:
        this_list = []
        to_do = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId=' +
            str(user['id']))
        json_todo = to_do.json()
        for item in json_todo:
            task_dict = {}
            task_dict["task"] = item['title']
            task_dict["completed"] = item['completed']
            task_dict["username"] = user['username']
            this_list.append(task_dict)

        general_dict[user['id']] = this_list

    json_f = 'todo_all_employees.json'
    with open(json_f, mode='w') as json_file:
        json.dump(general_dict, json_file)
