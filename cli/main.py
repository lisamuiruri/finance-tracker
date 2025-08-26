from database.db import Session
from models.user import User
from models.transaction import Transaction
from models.budget import Budget

session = Session()

def main_menu():
    while True:
        print("\n=== 🧾 Finance Tracker ===")
        print("1. Create a user")
        print("2. Add a transaction")
        print("3. Set a budget")
        print("4. View all transactions")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            create_user()
        elif choice == "2":
            add_transaction()
        elif choice == "3":
            set_budget()
        elif choice == "4":
            view_transactions()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

def create_user():
    name = input("Enter user name: ")
    email = input("Enter user email: ")

    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    print(f"✅ User '{name}' created successfully.")

def add_transaction():
    user_id = int(input("Enter user ID: "))
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    tx_type = input("Enter type ('income' or 'expense'): ")

    transaction = Transaction(user_id=user_id, amount=amount, category=category, type=tx_type)
    session.add(transaction)
    session.commit()
    print("✅ Transaction added.")

def set_budget():
    user_id = int(input("Enter user ID: "))
    category = input("Enter budget category: ")
    amount = float(input("Enter budget limit: "))
    month = input("Enter month (e.g., 'August 2025'): ")

    budget = Budget(user_id=user_id, category=category, amount_limit=amount, month=month)
    session.add(budget)
    session.commit()
    print("✅ Budget set.")

def view_transactions():
    user_id = int(input("Enter user ID: "))
    transactions = session.query(Transaction).filter_by(user_id=user_id).all()

    if not transactions:
        print("No transactions found.")
        return

    print("\nTransactions:")
    for t in transactions:
        print(f"- {t.date.date()} | {t.type.upper()} | {t.category} | ${t.amount}")

# Entry point
if __name__ == "__main__":
    main_menu()
