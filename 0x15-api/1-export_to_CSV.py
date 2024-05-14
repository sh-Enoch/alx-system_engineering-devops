#!/usr/bin/python3
"""A Script that, uses this REST API, for a given employee ID, returns."""

import csv
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

    u_name = users.get("username")
    name = users["name"]

    totalTasks = 0

    for done_tasks in json_req:
        if done_tasks['completed']:
            totalTasks += 1

    with open("{}.csv".format(idEmp), 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)

        for i in json_req:
            writer.writerow([idEmp, u_name, i.get('completed'),
                            i.get('title')])
