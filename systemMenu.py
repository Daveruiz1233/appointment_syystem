import add_appointment
import menus
import view_appointments


def display_menu(username):
    while True:
        choice = menus.system_menu_choice()

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
