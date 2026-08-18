expenses = []

while True:
    print("\n💰 Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: ₹"))
        category = input("Enter category: ")

        expenses.append({
            "name": name,
            "amount": amount,
            "category": category
        })

        print("✅ Expense added!")

    elif choice == "2":
        print("\n📋 Your Expenses:")

        if len(expenses) == 0:
            print("No expenses added yet.")
        else:
            total = 0

            for expense in expenses:
                print(
                    f"{expense['name']} - ₹{expense['amount']} "
                    f"({expense['category']})"
                )
                total += expense["amount"]

            print(f"\n💰 Total: ₹{total}")

    elif choice == "3":
        if len(expenses) == 0:
            print("No expenses to delete.")
        else:
            print("\nYour Expenses:")

            for i, expense in enumerate(expenses, 1):
                print(
                    f"{i}. {expense['name']} - "
                    f"₹{expense['amount']} ({expense['category']})"
                )

            delete_choice = int(
                input("Enter expense number to delete: ")
            )

            if 1 <= delete_choice <= len(expenses):
                deleted = expenses.pop(delete_choice - 1)
                print(f"🗑️ Deleted: {deleted['name']}")
            else:
                print("Invalid expense number.")

    elif choice == "4":
        print("👋 Thank you for using Expense Tracker!")
        break

    else:
        print("❌ Invalid choice. Please try again.")