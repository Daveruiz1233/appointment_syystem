import login
import signup


def main_menu():
    while True:
        print("\nEnter the number of your desired action.")
        print("[1] Login")
        print("[2] Signup")
        print("[3] Quit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            login.handle_login()
        elif choice == "2":
            signup.handle_signup()
        elif choice == "3":
            return
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
if __name__ == "__main__":
    main_menu()