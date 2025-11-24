# Student Budget Tracker

# Overview

The Student Budget Tracker is a Python-based command-line application designed to help university students manage their daily finances. It allows users to log expenses, view their spending history, and analyze their total expenditure.

# Features

1. Add Expenses: Record spending with category, amount, and description.
2. Data Persistence: Automatically saves data to a JSON file so nothing is lost on exit.
3. View History: Display a formatted list of all past transactions.
4. Analytics: Calculate total money spent and average transaction size.
5. Error Handling: Prevents crashes when invalid numbers are entered.

# Technologies Used

1. Language: Python 3.x
2. Modules: json, os, datetime, sys
3. Data Storage: JSON (File-based storage)
   
# How to Run

1. Ensure Python is installed on your system.
2. Download this repository.
3. Open a terminal/command prompt in the project folder.
4 Run the following command:

  python main.py
  
# Instructions for Testing

1. Select option 1 to add an expense (e.g., Food, 50, Lunch).
2. Select option 2 to view the list and confirm the entry appears.
3. Close the program and restart it to verify data is saved.
4. Try entering text (like "abc") into the Amount field to test error handling.
Close the program and restart it to verify data is saved.

Try entering text (like "abc") into the Amount field to test error handling.
