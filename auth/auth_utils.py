import json
import os


FILE = "users.json"


def load_users():

    if os.path.exists(FILE):

        with open(FILE, "r") as f:
            return json.load(f)

    return []


def save_users(users):

    with open(FILE, "w") as f:
        json.dump(users, f, indent=4)


def signup_user(name, email, password):

    users = load_users()

    for user in users:

        if user["email"] == email:
            return False

    users.append({

        "name": name,
        "email": email,
        "password": password
    })

    save_users(users)

    return True


def login_user(email, password):

    users = load_users()

    for user in users:

        if (
            user["email"] == email and
            user["password"] == password
        ):

            return user

    return None