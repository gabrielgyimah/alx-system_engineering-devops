#!/usr/bin/python3
"""API REQUESTS MODULE"""

import sys
import requests
import json


if __name__ == "__main__":
    """Returns information about his/her TODO list progress"""

    user_res = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}'
    )
    todo_res = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos'
    )

    if user_res.status_code == 200 and todo_res.status_code == 200:
        j_user_data = json.loads(user_res.text)
        j_todo_data = json.loads(todo_res.text)

        completed_tasks = [t for t in j_todo_data if t["completed"]]
        len_comptd = len(completed_tasks)
        len_total = len(j_todo_data)

        print(
            f"Employee {j_user_data['name']} is done with\
 tasks({len_comptd}/{len_total}):"
        )

        for val in completed_tasks:
            print(
                f"\
    {val['title']}"
            )
