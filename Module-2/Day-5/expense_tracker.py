expenses = []

def add_expense():
    """Add a new expense to the expense list."""
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
               print("Amount must be greater then 0")
               continue

            break

        except ValueError:
            print("Invalid amount. Please enter a valid amount")

    while True:
        category = input("Enter category: ").strip()

        if category:
            break

        print("Category cannot be empty")

    while True:    
        description = input("Enter description: ").strip()

        if description:
            break

        print("Description cannot be empty")


    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)

    print("Expense added sucessfully")


def view_expenses():
    """Display all recorded expenses."""
    if not expenses:
        print("No expense recorded yet ")
        return

    print("\n" + "=" * 60)
    print("               EXPENSES")
    print("=" * 60)

    print(f"{'No.':<5}{"Amount":<15}{"Category":<20}{"Description"}")
    print("-" * 60)

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index:<5}"
            f"₹{expense['amount']:<14.2f}"
            f"{expense['category']:<20}"
            f"{expense['description']}"
        )


def calculate_total():
    """Calculate and display the total expenses."""
    if not expenses:
        print("No expense recorded yet.")
        return

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("\n" + "=" * 40)
    print(f"Total expense: ₹{total:.2f}")
    print("=" * 40)    


def category_summary():
    """Calculate and display the total expenses."""
    if not expenses:
        print("No expense recorded yet.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    print("\n" + "=" * 45)
    print("               CATEGORY SUMMARY")
    print("=" * 45)

    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")

    print("=" * 45)    


def delete_expense():
    """Delete a selected expense after confirmation."""
    if not expenses:
        print("No expense recorded yet.")
        return

    view_expenses()

    try:
        expense_number = int(input("Enter expense number to delete: "))

        if 1 <= expense_number <= len(expenses):
            selected_expense = expenses[expense_number - 1]

            print(
                f"\nSelected: ₹{selected_expense['amount']:.2f} - "
                f"{selected_expense['category']} - "
                f"{selected_expense['description']}"
            )

        confirmation = input(
            "Are you sue yoou want to delete this expense? (y/n): "
        ).strip().lower()

        if confirmation == "y":
            deleted_expense = expenses.pop(expense_number - 1)

            print(
                    f"Deleted: ₹{deleted_expense['amount']:.2f} - "
                    f"{deleted_expense['category']} - "
                    f"{deleted_expense['description']}"
                )
            print("Expense deleted successfully:  ")
        elif confirmation == "n":
            print("Deletion cancelled.")

        else:
            print("Invalid choice. Deletion cancelled.")

    except ValueError:
        print("Please enter a valid number.")

def main():
    """Run the main Expense Tracker menu."""
    while True:
        print("\n" + "=" * 40)
        print("             EXPENSE TRACKER")
        print("=" * 40)
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category Summary")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            print("Thank you for using Expense Tracker")
            break
        else:
            print("Invalid option. Choose the valid option")              


if __name__ == "__main__":
    main()
