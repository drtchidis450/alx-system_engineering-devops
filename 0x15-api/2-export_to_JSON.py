#!/usr/bin/python3
""" 2. Output info from API as JSON file. """

import csv
import json
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
    user_name = infod.get('username')
    tasks = len(todod)

    count = 0
    for comp in todod:
        finished = comp.get('completed')
        if finished:
            count += 1

    dict_list = []
    json_dict = {}
    for task in todod:
        json_dict = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": infod.get('username')
            }
        dict_list.append(json_dict)
    all_data = {id: dict_list}

    with open('{}.json'.format(id), 'w') as emp_tasks:
        json.dump(all_data, emp_tasks)

    # print('Employee {} is done with tasks({}/{}):'.format(
    #     name, count, tasks))
    # for task in todod:
    #     completed = task.get('completed')
    #     if completed:
    #         title = task.get('title')
    #         print("\t {}".format(title))

    # with open('{}.csv'.format(id), 'w') as emp_tasks:
    #     emp_writer = csv.writer(emp_tasks, delimiter=',', quotechar='"',
    #                             quoting=csv.QUOTE_ALL)
    #     for task in todod:
    #         uid = task.get('userId')
    #         comp = task.get('completed')
    #         title = task.get('title')
    #         write_list = [uid, user_name, comp, title]
    #         emp_writer.writerow(write_list)
