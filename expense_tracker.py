import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


expenses = load_expenses()

while True:
    print("\n" + "=" * 35)
    print("        💰 EXPENSE TRACKER")
    print("=" * 35)
    print("1. ➕ Add Expense")
    print("2. 📋 View Expenses")
    print("3. 💰 Total Spending")
    print("4. 📊 Category Summary")
    print("5. 🗑️ Delete Expense")
    print("6. ❌ Exit")
    print("=" * 35)

    choice = input("Enter your choice: ")

    # Add Expense
    if choice == "1":
        name = input("Enter expense name: ")

        try:
            amount = float(input("Enter amount: ₹"))
        except ValueError:
            print("❌ Please enter a valid amount.")
            continue

        category = input("Enter category: ")

        expense = {
            "name": name,
            "amount": amount,
            "category": category
        }

        expenses.append(expense)
        save_expenses(expenses)

        print("✅ Expense added successfully!")

    # View Expenses
    elif choice == "2":
        print("\n📋 YOUR EXPENSES")
        print("-" * 35)

        if not expenses:
            print("No expenses added yet.")
        else:
            for i, expense in enumerate(expenses, 1):
                print(
                    f"{i}. {expense['name']} - "
                    f"₹{expense['amount']:.2f} "
                    f"({expense['category']})"
                )

    # Total Spending
    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)

        print("\n💰 TOTAL SPENDING")
        print("-" * 35)
        print(f"Total: ₹{total:.2f}")

    # Category Summary
    elif choice == "4":
        print("\n📊 CATEGORY SUMMARY")
        print("-" * 35)

        if not expenses:
            print("No expenses added yet.")
        else:
            categories = {}

            for expense in expenses:
                category = expense["category"]
                categories[category] = categories.get(category, 0) + expense["amount"]

            for category, amount in categories.items():
                print(f"{category}: ₹{amount:.2f}")

    # Delete Expense
    elif choice == "5":
        if not expenses:
            print("No expenses to delete.")
        else:
            print("\n🗑️ YOUR EXPENSES")

            for i, expense in enumerate(expenses, 1):
                print(
                    f"{i}. {expense['name']} - "
                    f"₹{expense['amount']:.2f} "
                    f"({expense['category']})"
                )

            try:
                delete_choice = int(
                    input("Enter expense number to delete: ")
                )

                if 1 <= delete_choice <= len(expenses):
                    deleted = expenses.pop(delete_choice - 1)
                    save_expenses(expenses)

                    print(f"✅ Deleted: {deleted['name']}")
                else:
                    print("❌ Invalid expense number.")

            except ValueError:
                print("❌ Please enter a valid number.")

    # Exit
    elif choice == "6":
        print("\n👋 Thank you for using Expense Tracker!")
        break

    else:
        print("❌ Invalid choice. Please try again.")