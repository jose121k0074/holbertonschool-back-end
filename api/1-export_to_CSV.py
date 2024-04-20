#!/usr/bin/python3
"""given employee ID returns all his todo list"""


import csv
import requests
import sys


if __name__ == "__main__":
    to_do = requests.get('https://jsonplaceholder.typicode.com/todos?userId=' +
                         sys.argv[1])
    names = requests.get('https://jsonplaceholder.typicode.com/users/' +
                         sys.argv[1])

    json_todo = to_do.json()
    json_names = names.json()

    csv_f = sys.argv[1] + '.csv'
    with open(csv_f, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
        for element in json_todo:
            csv_writer.writerow([element['userId'], json_names['username'],
                                 element['completed'], element['title']])
