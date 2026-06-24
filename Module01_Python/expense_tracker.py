#Functions, menu loop, dict accumulation, budget comparison

def add_expense(expenses, category, amount, description):
    expenses.append({
        "category": category,
        "amount": amount,
        "description": description,
    })


def get_summary(expenses):
    if not expenses:
        return {}

    summary = {}
    for expense in expenses:
        cat = expense["category"]
        summary[cat] = summary.get(cat, 0) + expense["amount"]
    return summary


def display_expenses(expenses):
    if not expenses:
        print("  No expenses recorded yet.")
        return

    print(f"\n  {'#':<4} {'Category':<15} {'Amount (Rs)':<14} {'Description'}")
    print("  " + "-" * 55)
    for i, e in enumerate(expenses, 1):
        print(f"  {i:<4} {e['category']:<15} {e['amount']:<14.2f} {e['description']}")


def display_summary(expenses, budget):
    summary = get_summary(expenses)
    total = sum(e["amount"] for e in expenses)

    print("\n--- Summary by Category ---")
    for category, amount in sorted(summary.items()):
        print(f"  {category:<15}: Rs {amount:.2f}")

    print(f"\n  Total Spent : Rs {total:.2f}")
    print(f"  Budget      : Rs {budget:.2f}")
    remaining = budget - total
    if remaining >= 0:
        print(f"  Remaining   : Rs {remaining:.2f}  (On track)")
    else:
        print(f"  Over Budget : Rs {abs(remaining):.2f}  (Exceeded!)")


CATEGORIES = ["Food", "Transport", "Utilities", "Entertainment", "Health", "Other"]


def main():
    print("=== Expense Tracker ===\n")

    while True:
        try:
            budget = float(input("Set your monthly budget (Rs): "))
            if budget > 0:
                break
            print("Budget must be a positive number.")
        except ValueError:
            print("Please enter a valid number.")

    expenses = []

    while True:
        print("\n--- Menu ---")
        print("  1. Add expense")
        print("  2. View all expenses")
        print("  3. View summary")
        print("  4. Exit")

        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            print("\nCategories:", ", ".join(CATEGORIES))
            category = input("Category: ").strip().capitalize()
            if category not in CATEGORIES:
                category = "Other"

            while True:
                try:
                    amount = float(input("Amount (Rs): "))
                    if amount > 0:
                        break
                    print("Amount must be positive.")
                except ValueError:
                    print("Please enter a valid number.")

            description = input("Description: ").strip() or "N/A"
            add_expense(expenses, category, amount, description)
            print(f"Expense of Rs {amount:.2f} added under '{category}'.")

        elif choice == "2":
            print("\n--- All Expenses ---")
            display_expenses(expenses)

        elif choice == "3":
            display_summary(expenses, budget)

        elif choice == "4":
            print("\nFinal Summary:")
            display_summary(expenses, budget)
            print("\nGoodbye!")
            break

        else:
            print("Invalid option. Please choose 1-4.")


if __name__ == "__main__":
    main()