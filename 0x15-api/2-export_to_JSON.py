#!/usr/bin/python3
""" a Python script that, for a given employee ID,
returns information about his/her TODO list progress
"""
import json
import requests
import sys


if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users/"
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    response_user = requests.get(user_url + "{}".format(sys.argv[1])).json()
    response_todo = requests.get(
        todos_url, params={"userId": sys.argv[1]}).json()

    # Fetch user data
    response_user = requests.get(user_url + sys.argv[1]).json()

    # Create a list to hold all tasks for the user
    all_tasks = []

    for task in response_todo:
        # Create a dictionary for each task
        task_info = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": response_user.get("username")
        }

    # Append the task dictionary to the list
    all_tasks.append(task_info)

    # Create a dictionary with the user ID as key and the
    # list of tasks as value
    user_tasks = {sys.argv[1]: all_tasks}

    with open("{}.json".format(sys.argv[1]), "w") as f:
        json.dump(user_tasks, f)
