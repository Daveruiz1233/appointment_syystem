import login
import menus
import signup
import systemMenu


def main_menu():
    while True:
        choice = menus.main_menu_choice()

        if choice == "1":
            username = login.handle_login()
            if username:
                systemMenu.display_menu(username)
        elif choice == "2":
            signup.handle_signup()
        elif choice == "3":
            return
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
if __name__ == "__main__":
    main_menu()