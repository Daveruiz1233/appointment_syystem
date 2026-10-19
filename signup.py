import json
import menus

def handle_signup():

    with open("users.json", "r") as file:
        loaded_users = json.load(file)

    while True:
        username, password = menus.signup_credentials()

        if not username or not password:
            print("Username and password cannot be empty.")
            continue

        if any(user["username"] == username for user in loaded_users):
            print("Username already exists.")
            continue

        loaded_users.append({"username": username, "password": password})
        with open("users.json", "w") as file:
            json.dump(loaded_users, file, indent=4)
        return True