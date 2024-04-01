#!/usr/bin/python3
"""Python script given emp_ID, returns information of TODO list progress."""
import json
from sys import argv
import requests


if __name__ == "__main__":
    emp_id = argv[1]

    empUrl = ("https://jsonplaceholder.typicode.com/users/{}/todos"
              .format(emp_id))

    nameUrl = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)

    sessionGet = requests.session()

    employee = sessionGet.get(empUrl)
    name = sessionGet.get(nameUrl)

    json_form = employee.json()
    name_json = name.json()['name']

    total_tasks = 0

    for task in json_form:
        if task['completed']:
            total_tasks += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(name_json, total_tasks, len(json_form)))

    for done_task in json_form:
        if done_task['completed']:
            print("\t" + done_task.get('title'))
