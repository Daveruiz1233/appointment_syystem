import json

import add_appointment


APPOINTMENTS_FILE = "appointments.json"
CALENDAR_FILE = "calendar.json"


def load_json(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_appointments(appointments):
    with open(APPOINTMENTS_FILE, "w") as file:
        json.dump(appointments, file, indent=4)


def get_user_appointments(username):
    return [
        appointment
        for appointment in load_json(APPOINTMENTS_FILE)
        if appointment.get("username") == username
    ]


def show_user_appointments(username):
    appointments = get_user_appointments(username)
    if not appointments:
        print("\nYou have no appointments.")
        return appointments

    print("\nYour appointments:")
    for number, appointment in enumerate(appointments, start=1):
        print(f"{number}. {appointment['date']}")
    return appointments


def change_appointment(username, selected_appointment):
    all_appointments = load_json(APPOINTMENTS_FILE)
    appointment_removed = False
    appointments_without_selected = []
    for appointment in all_appointments:
        if (
            not appointment_removed
            and appointment.get("username") == username
            and appointment.get("date") == selected_appointment.get("date")
        ):
            appointment_removed = True
            continue
        appointments_without_selected.append(appointment)

    available_dates = add_appointment.get_available_november_dates(
        appointments_without_selected
    )

    if not available_dates:
        print("No dates are available.")
        return

    new_date = add_appointment.show_dates_paged(available_dates)
    if new_date is None:
        return

    for appointment in all_appointments:
        if (
            appointment.get("username") == username
            and appointment.get("date") == selected_appointment.get("date")
        ):
            appointment["date"] = new_date
            break
    save_appointments(all_appointments)
    print(f"Appointment changed to {new_date}.")


def appointments_menu(username):
    while True:
        appointments = show_user_appointments(username)
        if not appointments:
            input("Press Enter to return to the system menu.")
            return

        choice = input(
            "\nSelect an appointment number, or enter q to return: "
        ).strip().lower()
        if choice == "q":
            return
        if not choice.isdigit() or not 1 <= int(choice) <= len(appointments):
            print("Invalid selection.")
            continue

        selected_appointment = appointments[int(choice) - 1]
        action = input(
            "[1] Cancel appointment\n"
            "[2] Change date\n"
            "[3] Back\n"
            "Choose an action: "
        ).strip()

        if action == "1":
            all_appointments = load_json(APPOINTMENTS_FILE)
            all_appointments.remove(selected_appointment)
            save_appointments(all_appointments)
            print("Appointment cancelled.")
        elif action == "2":
            change_appointment(username, selected_appointment)
        elif action != "3":
            print("Invalid choice.")
