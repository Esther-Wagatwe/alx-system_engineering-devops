#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees
Export data in the JSON format."""

import requests
import sys


if __name__ == '__main__':
    employee_Id = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employee_Id

    response = requests.get(url)
    username = response.json().get('username')

    todo_Url = url + "/todos"
    response = requests.get(todo_Url)
    tasks = response.json()

    with open('{}.csv'.format(employee_Id), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employee_Id, username, task.get('completed'),
                               task.get('title')))
