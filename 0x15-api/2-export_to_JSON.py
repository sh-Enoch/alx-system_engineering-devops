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

    file_ = "{}.json".format(idEmp)
    
    #json_string = json_req.dumps(json_req)
    with open(file_, 'w') as myfile:
        myfile.dump(json_req)
