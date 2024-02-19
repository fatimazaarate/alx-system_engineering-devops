#!/usr/bin/python3
""" a Python script that, for a given employee ID,
returns information about his/her TODO list progress
"""
import json
import requests
import sys


if __name__ == "__main__":
    user = "https://jsonplaceholder.typicode.com/users/"
    todos = "https://jsonplaceholder.typicode.com/todos"
    response_user = requests.get(user + "{}".format(sys.argv[1])).json()
    response_todo = requests.get(todos, params={"userId": sys.argv[1]}).json()

    all_in_all = []
    request = requests.get('https://jsonplaceholder.typicode.com//todos')\
        .json()

    for task in request:
        if (task.get("userId") == int(sys.argv[1])):
            temp = {}
            temp["task"] = task.get("title")
            temp["completed"] = task.get("completed")
            temp["username"] = response_user
            all_in_all.append(temp)

    with open("{}.json".format(sys.argv[1]), "a") as f:
        json.dump({sys.argv[1]: all_in_all}, f)
