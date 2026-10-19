def main_menu_choice():
    print("\n\n\n\n\nWelcome to the appointment system Login menu.")
    print("[1] Login")
    print("[2] Signup")
    print("[3] Quit")
    return input("Enter your choice: ").strip()


def login_credentials():
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    return username, password


def signup_credentials():
    username = input("Choose a username: ").strip()
    password = input("Choose a password: ").strip()
    return username, password


def retry_login():
    return input("Try again? (y/n): ").strip().lower()


def system_menu_choice():
    print("\n\n\n\n\nWelcome to the appointment system menu")
    print("[1] add an appointment")
    print("[2] view appointments")
    print("[3] Logout")
    return input("Enter your choice: ").strip()


def select_date(dates, page_size):
    page = 0
    total_pages = (len(dates) + page_size - 1) // page_size

    while True:
        start = page * page_size
        chunk = dates[start:start + page_size]

        print(f"\n\n\n\n\nAvailable dates (page {page + 1}/{total_pages})")
        for number, date in enumerate(chunk, start=1):
            print(f"{number}. {date}")

        choice = input(
            "[1-5] pick a date, [n]ext, [p]revious, [q]uit: "
        ).strip().lower()

        if choice == "n":
            if page < total_pages - 1:
                page += 1
            else:
                print("You're on the last page.")
        elif choice == "p":
            if page > 0:
                page -= 1
            else:
                print("You're on the first page.")
        elif choice == "q":
            return
        elif choice.isdigit() and 1 <= int(choice) <= len(chunk):
            return chunk[int(choice) - 1]
        else:
            print("Invalid input.")


def return_to_system_menu():
    input("Press Enter to return to the system menu.")


def select_appointment(appointments):
    print("\n\n\nYour appointments:")
    for number, appointment in enumerate(appointments, start=1):
        print(f"{number}. {appointment['date']}")
    return input(
        "\nSelect an appointment number, or enter q to return: "
    ).strip().lower()


def appointment_action():
    return input(
        "[1] Cancel appointment\n"
        "[2] Change date\n"
        "[3] Back\n"
        "Choose an action: "
    ).strip()
