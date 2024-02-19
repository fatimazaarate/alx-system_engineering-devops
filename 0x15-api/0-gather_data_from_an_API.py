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
    """keeps track of num of completed tasks"""
    counter = 0
    """stores num of the users tasks"""
    len_tasks = len(response_todo)

    name = response_user.get("name")
    for task in response_todo:
        if task.get("completed"):
            counter += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(name, counter, len_tasks))
    for task in response_todo:
        if task.get("completed"):
            print("\t {}".format(task.get("title")))
