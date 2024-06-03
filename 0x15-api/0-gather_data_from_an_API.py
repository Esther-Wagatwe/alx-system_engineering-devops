#!/usr/bin/python3
"""Module that uses REST API, for a given employee ID, returns information
about his/her TODO list progress."""
import requests
import sys


if __name__ == '__main__':
    employee_Id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{employee_Id}'

    response = requests.get(url)
    employee_name = response.json().get('name')

    todo_Url = url + "/todos"
    response = requests.get(todo_Url)
    tasks = response.json()
    completed_tasks = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            completed_tasks += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, completed_tasks, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
