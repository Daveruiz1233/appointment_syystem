import json
from datetime import datetime

import menus

PAGE_SIZE = 5
MONTH_PREFIX = "11"      # November 2026

def load_json(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def get_available_november_dates(appointments=None):
    calendar = load_json("calendar.json")
    if appointments is None:
        appointments = load_json("appointments.json")
    taken = {
        datetime.strptime(appointment["date"], "%m-%d-%Y").strftime("%m-%d-%Y")
        for appointment in appointments
    }
    return [d for d in calendar if d.startswith(MONTH_PREFIX) and d not in taken]

def add_menu(username):

    dates = get_available_november_dates()
    if not dates:
        print("No available dates in November.")
        return

    selected = menus.select_date(dates, PAGE_SIZE)
    if selected:
        appointments = load_json("appointments.json")
        appointments.append({"username": username, "date": selected})
        with open("appointments.json", "w") as file:
            json.dump(appointments, file, indent=4)
        print(f"You selected {selected}.")