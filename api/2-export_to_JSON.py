#!/usr/bin/python3
"""given employee ID returns all his todo list"""


import json
import requests
import sys


if __name__ == "__main__":
    to_do = requests.get('https://jsonplaceholder.typicode.com/todos?userId=' +
                         sys.argv[1])
    names = requests.get('https://jsonplaceholder.typicode.com/users/' +
                         sys.argv[1])

    json_todo = to_do.json()
    json_names = names.json()

    my_dict = {}
    this_list = []

    for item in json_todo:
        task_dict = {}
        task_dict["task"] = item['title']
        task_dict["completed"] = item['completed']
        task_dict["username"] = json_names['username']
        this_list.append(task_dict)

    my_dict[sys.argv[1]] = this_list

    json_f = sys.argv[1] + '.json'
    with open(json_f, mode='w') as json_file:
        json.dump(my_dict, json_file)
