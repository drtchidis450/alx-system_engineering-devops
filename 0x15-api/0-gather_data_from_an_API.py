#!/usr/bin/python3
""" 0. Input employee ID, output their todo list via API. """

import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    info = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(
        id))
    todo = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id))

    infod = info.json()
    todod = todo.json()

    name = infod.get('name')
    tasks = len(todod)

    count = 0
    for comp in todod:
        finished = comp.get('completed')
        if finished:
            count += 1

    print('Employee {} is done with tasks({}/{}):'.format(name, count, tasks))
    for task in todod:
        completed = task.get('completed')
        if completed:
            title = task.get('title')
            print("\t {}".format(title))
