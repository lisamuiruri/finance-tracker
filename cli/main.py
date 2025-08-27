import re
from database.db import Session
from models.user import User
from models.transaction import Transaction
from models.budget import Budget

session = Session()

# Data structures for validation
VALID_TRANSACTION_TYPES = ['income', 'expense']
CATEGORIES = ['Food', 'Transport', 'Entertainment', 'Bills', 'Shopping', 'Other']
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']

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
    try:
        name = input("Enter user name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return
        
        email = input("Enter user email: ").strip()
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            print("Invalid email format.")
            return

        user = User(name=name, email=email)
        session.add(user)
        session.commit()
        print(f"User '{name}' created successfully with ID: {user.id}")
    except Exception as e:
        session.rollback()
        print(f"Error creating user: {e}")

def add_transaction():
    try:
        user_id_str = input("Enter user ID: ").strip()
        if not user_id_str.isdigit():
            print("User ID must be a number.")
            return
        user_id = int(user_id_str)
        
        amount_str = input("Enter amount: ").strip()
        if amount_str.lower() in ['nan', 'inf', '-inf']:
            print("Invalid amount value.")
            return
        amount = float(amount_str)
        if amount <= 0:
            print("Amount must be positive.")
            return
        
        print(f"Categories: {', '.join(CATEGORIES)}")
        category = input("Enter category: ").strip()
        if not category:
            print("Category cannot be empty.")
            return
        
        tx_type = input("Enter type ('income' or 'expense'): ").strip().lower()
        if tx_type not in VALID_TRANSACTION_TYPES:
            print(f"Type must be one of: {', '.join(VALID_TRANSACTION_TYPES)}")
            return

        transaction = Transaction(user_id=user_id, amount=amount, category=category, type=tx_type)
        session.add(transaction)
        session.commit()
        print("Transaction added.")
    except ValueError:
        print("Invalid number format.")
    except Exception as e:
        session.rollback()
        print(f"Error adding transaction: {e}")

def set_budget():
    try:
        user_id_str = input("Enter user ID: ").strip()
        if not user_id_str.isdigit():
            print("User ID must be a number.")
            return
        user_id = int(user_id_str)
        
        print(f"Categories: {', '.join(CATEGORIES)}")
        category = input("Enter budget category: ").strip()
        if not category:
            print("Category cannot be empty.")
            return
        
        amount_str = input("Enter budget limit: ").strip()
        if amount_str.lower() in ['nan', 'inf', '-inf']:
            print("Invalid amount value.")
            return
        amount = float(amount_str)
        if amount <= 0:
            print("Budget limit must be positive.")
            return
        
        print(f"Months: {', '.join(MONTHS)}")
        month = input("Enter month: ").strip()
        if not month:
            print("Month cannot be empty.")
            return

        budget = Budget(user_id=user_id, category=category, limit=amount, month=month)
        session.add(budget)
        session.commit()
        print("✅ Budget set.")
    except ValueError:
        print("Invalid number format.")
    except Exception as e:
        session.rollback()
        print(f"Error setting budget: {e}")

def view_transactions():
    try:
        user_id_str = input("Enter user ID: ").strip()
        if not user_id_str.isdigit():
            print("User ID must be a number.")
            return
        user_id = int(user_id_str)
        
        transactions = session.query(Transaction).filter_by(user_id=user_id).all()

        if not transactions:
            print("No transactions found.")
            return

        # Using data structures: dict for summary, list for transactions
        summary = {'income': 0, 'expense': 0}
        transaction_list = []
        
        for t in transactions:
            summary[t.type] += t.amount
            transaction_tuple = (t.date.date(), t.type.upper(), t.category, t.amount)
            transaction_list.append(transaction_tuple)

        print("\nTransactions:")
        for date, tx_type, category, amount in transaction_list:
            print(f"- {date} | {tx_type} | {category} | ${amount}")
        
        print(f"\nSummary: Income: ${summary['income']}, Expenses: ${summary['expense']}, Balance: ${summary['income'] - summary['expense']}")
    except Exception as e:
        print(f" Error viewing transactions: {e}")

# Entry point
if __name__ == "__main__":
    main_menu()
