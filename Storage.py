import json
import os
from datetime import datetime

# File where data will be stored
DATA_FILE = "expenses.json"


def load_expenses():
    """Loads expenses from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []  # Return empty list if file doesn't exist

    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []


def save_expense(category, amount, description):
    """Saves a new expense to the file."""
    expenses = load_expenses()

    new_entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(new_entry)

    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)


def delete_expense():
    """Deletes the last added expense."""
    expenses = load_expenses()
    if expenses:
        expenses.pop()  # Removes the last item
        with open(DATA_FILE, 'w') as file:
            json.dump(expenses, file, indent=4)