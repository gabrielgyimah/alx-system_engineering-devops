#!/usr/bin/python3
"""Dictionary JSON Storage Module"""

import json
import requests


if __name__ == "__main__":
    """Stores TODO list progress to a json file."""
    base_url = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(base_url)
    if users.status_code == 200:
        with open("todo_all_employees.json", 'w') as json_file:
            objs = {}
            for user in users.json():
                todo_url = '{}{}/todos'.format(base_url, user['id'])
                todos = requests.get(todo_url)
                name = user['username']
                obj_props = []
                user_id = ''
                for task in todos.json():
                    obj = {
                            "username": name,
                            "task": task["title"],
                            "completed": task["completed"]}
                    user_id = task["userId"]
                    obj_props.append(obj)
                objs[user_id] = obj_props
            json.dump(objs, json_file)
