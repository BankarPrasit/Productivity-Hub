import json
import os

FILE = "data/tasks.json"

def load_tasks():

    if os.path.exists(FILE):

        try:
            with open(FILE, "r") as f:
                return json.load(f)

        except:
            return []

    return []

def save_tasks(tasks):

    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)