import json
import menus

def handle_login():
    with open("users.json", "r") as file:
        loaded_users = json.load(file)

    while True:
        username, password = menus.login_credentials()
        is_authenticated = any(
            user["username"] == username and user["password"] == password
            for user in loaded_users
        )

        if is_authenticated:
            return username

        print("Login failed")
        choice = menus.retry_login()
        if choice != "y":
            return
