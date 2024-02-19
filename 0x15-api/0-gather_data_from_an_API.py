#!/usr/bin/python3
"""a Python script that returns information about his/her TODO list progress."""

import requests
import sys

def employee_todo(employee_id):
    employee_resp = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee_data = employee_resp.json()
    employee_name = employee_data['name']

    todo_resp = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todo_data = todo_resp.json()

    completed_tasks = [task for task in todo_data if task['completed']]
    number_compl_tasks = len(completed_tasks)
    total_num_tasks = len (todo_data)

    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_num_tasks}):")

    for task in completed_tasks:
        print(f"\t{task['title']}")

    if __name__ == "__main__":
        employee_id = int(sys.argv[1])
        employee_todo(employee_id)
