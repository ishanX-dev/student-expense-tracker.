
expenses = []

while True:
    print("\n--- Student Expense Tracker ---")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total")
    print("4. Show number of expenses")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Expense name: ")

        try:
            amount = float(input("Amount in rupees: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                expenses.append({
                    "name": name,
                    "amount": amount
                })
                print("Expense added successfully!")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded yet.")
        else:
            for expense in expenses:
                print(f'{expense["name"]} - ₹{expense["amount"]:.2f}')

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print(f"Total spending: ₹{total:.2f}")

    elif choice == "4":
        print(f"Number of expenses: {len(expenses)}")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
