import add_appointment
import view_appointments


def display_menu(username):
    while True:
        print("\nWelcome to the appointment system menu")
        print("[1] add an appointment")
        print("[2] view appointments")
        print("[3] Logout")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_appointment.add_menu(username)
        elif choice == "2":
            view_appointments.appointments_menu(username)
        elif choice == "3":
            return
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def handle_menu(username):
    display_menu(username)
