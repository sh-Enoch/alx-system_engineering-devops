#!/usr/bin/python3
"""A Script that, uses this REST API, for a given employee ID, returns."""


import json
import requests
from sys import argv


if __name__ == "__main__":

    idEmp = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(idEmp)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(idEmp)

    employee = requests.get(idURL)
    employeeName = requests.get(nameURL)

    json_req = employee.json()
    users = employeeName.json()

    name = users["name"]

    totalTasks = 0

    for done_tasks in json_req:
        if done_tasks['completed']:
            totalTasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(name, totalTasks, len(json_req)))

    for done_tasks in json_req:
        if done_tasks['completed']:
            print("\t " + done_tasks.get('title'))
