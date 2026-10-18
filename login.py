import json
import systemMenu

def login_menu():

    username = input("Username: ").strip()
    password = input("Password: ").strip()
    return username, password

def handle_login():
    with open("users.json", "r") as file:
        loaded_users = json.load(file)

    while True:
        username, password = login_menu()
        is_authenticated = any(
            user["username"] == username and user["password"] == password
            for user in loaded_users
        )

        if is_authenticated:
            systemMenu.display_menu(username)
            return username

        print("Login failed")
        choice = input("Try again? (y/n): ").strip().lower()
        if choice != "y":
            return True
