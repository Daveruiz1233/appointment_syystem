import json
from datetime import datetime

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

def show_dates_paged(dates):
    page = 0
    total_pages = (len(dates) + PAGE_SIZE - 1) // PAGE_SIZE   # round up

    while True:
        start = page * PAGE_SIZE
        chunk = dates[start:start + PAGE_SIZE]

        print(f"\nAvailable dates (page {page + 1}/{total_pages})")
        for number, date in enumerate(chunk, start=1):
            print(f"{number}. {date}")

        choice = input("[1-5] pick a date, [n]ext, [p]revious, [q]uit: ").strip().lower()

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

def add_menu(username):

    dates = get_available_november_dates()
    if not dates:
        print("No available dates in November.")
        return

    selected = show_dates_paged(dates)
    if selected:
        appointments = load_json("appointments.json")
        appointments.append({"username": username, "date": selected})
        with open("appointments.json", "w") as file:
            json.dump(appointments, file, indent=4)
        print(f"You selected {selected}.")