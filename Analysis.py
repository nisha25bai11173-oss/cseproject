from Storage import load_expenses


def list_all_expenses():
    """Prints all expenses in a readable format."""
    expenses = load_expenses()
    if not expenses:
        print("\n📭 No expenses recorded yet.")
        return

    print(f"\n{'Date':<20} | {'Category':<10} | {'Amount':<10} | {'Description'}")
    print("-" * 60)
    for expense in expenses:
        print(f"{expense['date']:<20} | {expense['category']:<10} | Rs{expense['amount']:<9} | {expense['description']}")


def show_summary():
    """Calculates and shows total spending."""
    expenses = load_expenses()
    total_spent = sum(item['amount'] for item in expenses)
    count = len(expenses)

    print("\n--- 📊 Financial Summary ---")
    print(f"Total Transactions: {count}")
    print(f"Total Spent: Rs{total_spent:.2f}")

    if count > 0:
        print(f"Average Spend: Rs{total_spent / count:.2f}")