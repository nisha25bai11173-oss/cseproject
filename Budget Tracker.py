import sys
from Storage import load_expenses, save_expense, delete_expense
from Analysis import show_summary, list_all_expenses


def print_menu():
    print("\n--- Student Budget Tracker ---")
    print("1. Add a New Expense")
    print("2. View All Expenses")
    print("3. View Spending Summary")
    print("4. Delete Last Expense")
    print("5. Exit")
    print("------------------------------")


def main():
    # Load existing data when program starts
    print("Welcome! Loading your data...")

    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            category = input("Enter Category (Food, Transport, Books, Fun): ")
            try:
                amount = float(input("Enter Amount: "))
                description = input("Enter Description (e.g., Lunch, Bus Ticket): ")
                save_expense(category, amount, description)
                print("✅ Expense saved successfully!")
            except ValueError:
                print("❌ Error: Please enter a valid number for the amount.")

        elif choice == '2':
            list_all_expenses()

        elif choice == '3':
            show_summary()

        elif choice == '4':
            delete_expense()
            print("✅ Last expense deleted.")

        elif choice == '5':
            print("Goodbye! Saving data...")
            sys.exit()

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()