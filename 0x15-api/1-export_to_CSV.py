#!/usr/bin/python3
""" a Python script that, for a given employee ID,
returns information about his/her TODO list progress
and  export data in the CSV format."""
import requests
import sys


if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users/"
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    response_user = requests.get(user_url + "{}".format(sys.argv[1])).json()
    response_todo = requests.get(
        todos_url, params={"userId": sys.argv[1]}).json()

    task_status = []
    task_title = []

    username = response_user.get('username')

    for todo in response_todo:
        task_status.append(todo.get('completed'))
        task_title.append(todo.get('title'))
    with open("{}.csv".format(sys.argv[1]), "a") as f:
        for status, title in zip(task_status, task_title):
            print('"{}","{}","{}","{}"'
                  .format(sys.argv[1], username, status, title), file=f)
