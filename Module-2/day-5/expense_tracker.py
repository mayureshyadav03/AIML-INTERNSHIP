expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)

    print("Expense added sucessfully")


def view_expenses():
    if not expenses:
        print("No expense recorded yet ")
        return

    print("\n------EXPENSES------")

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. ₹{expense['amount']:.2f}-"
            f"{expense['category']}-"
            f"{expense['description']}"
        )


def calculate_total():
    if not expenses:
        print("No expense recorded yet.")
        return

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total expense: ₹{total:.2f}")    


def category_summary():
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

    print("\n--------CATEGORY SUMMARY--------")

    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")


def delete_expense():
    if not expenses:
        print("No expense recorded yet.")
        return

    view_expenses()
    try:
        idx = int(input("Enter expense number to delete: "))
        if 1 <= idx <= len(expenses):
            removed = expenses.pop(idx - 1)
            print(f"Removed expense: ₹{removed['amount']:.2f} - {removed['category']} - {removed['description']}")
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n=================================")
        print("         EXPENSE TRACKER")
        print("==================================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category Summary")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Enter your choice: ")

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
