#!/usr/bin/python3
"""Module that uses REST API, for a given employee ID, returns information
about his/her TODO list progress."""
from requests import get
from sys import argv

def todo(employer_id):
    """ Send request for employee's
        to do list to API
    """
    total_tasks = 0
    completed_tasks = 0
    url_user = 'https://jsonplaceholder.typicode.com/users/'
    url_todo = 'https://jsonplaceholder.typicode.com/todos/'

    # check if user exists
    user = get(url_user + employer_id).json().get('name')

    if user:
        params = {'userId': employer_id}
        #  get all tasks
        tasks = get(url_todo, params=params).json()
        if tasks:
            total_tasks = len(tasks)
            #  get number of completed tasks
            params.update({'completed': 'true'})
            completed = len(get(url_todo, params=params).json())

        print("Employee {} is done with tasks({}/{}):".format(
            user, completed_tasks, total_tasks))
        for task in tasks:
            if task.get('completed') is True:
                print("\t {}".format(task.get('title')))


if __name__ == '__main__':
    if len(argv) > 1:
        todo(argv[1])
