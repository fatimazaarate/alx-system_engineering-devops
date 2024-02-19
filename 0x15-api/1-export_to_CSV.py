#!/usr/bin/python3
""" a Python script that, for a given employee ID,
returns information about his/her TODO list progress."""
import requests
import sys


if __name__ == "__main__":
    user = "https://jsonplaceholder.typicode.com/users/"
    todos = "https://jsonplaceholder.typicode.com/todos"
    response_user = requests.get(user + "{}".format(sys.argv[1])).json()
    response_todo = requests.get(todos, params={"userId": sys.argv[1]}).json()

    task_status = []
    task_title = []

    request = requests.get('https://jsonplaceholder.typicode.com//todos')\
        .json()

    for test in request:
        if test.get('userId') == int(sys.argv[1]):
            task_status.append(test.get('completed'))
            task_title.append(test.get('title'))
    with open("{}.csv".format(sys.argv[1]), "a") as f:
        for status, title in zip(task_status, task_title):
            print('"{}","{}","{}","{}"'
                  .format(sys.argv[1], response_user, status, title), file=f)
