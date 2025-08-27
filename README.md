# Finance Tracker CLI
A Python-based command-line application that allows users to track income, expenses, and budgets. This project was built as part of Phase 3 at Moringa School, focusing on CLI application design, Object-Oriented Programming (OOP), and SQLAlchemy ORM.

# Project Description
This app helps users manage their finances by:
 Creating a personal user profile
 Recording income and expense transactions
 Setting monthly budgets by category
 Viewing all their transaction history with summaries

The data is stored locally in a SQLite database (`finance_tracker.db`) using SQLAlchemy ORM.

# Technologies Used
 **Python 3.8+**
 **SQLAlchemy** (ORM)
 **SQLite** (Database)
 **Pipenv** (Virtual environment and dependency management)
 **Pytest** (Testing framework)

# Installation & Setup

 **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd finance-tracker
   ```

 **Install dependencies:**
   ```bash
   pipenv install
   ```

 **Set up the database:**
   ```bash
   pipenv run python seed.py
   ```

 **Run the application:**
   ```bash
   PYTHONPATH=. pipenv run python -m cli.main
   ```

# CLI Usage Guide

The application provides an interactive menu with the following options:

# 1. Create a User
 **Function:** `create_user()`
 **Purpose:** Creates a new user profile in the system
 **Input validation:** Validates name (non-empty) and email format
 **Output:** Returns user ID for future transactions

# 2. Add a Transaction
 **Function:** `add_transaction()`
 **Purpose:** Records income or expense transactions
 **Validation:** 
   User ID must be numeric
   Amount must be positive number
   Type must be 'income' or 'expense'
   Category cannot be empty
   **Categories:** Food, Transport, Entertainment, Bills, Shopping, Other

# 3. Set a Budget
 **Function:** `set_budget()`
 **Purpose:** Sets monthly spending limits by category **Validation:**
   User ID must be numeric
   Budget limit must be positive
   Category and month cannot be empty
 **Available months:** January through December

# 4. View All Transactions
 **Function:** `view_transactions()`
 **Purpose:** Displays user's transaction history with summary
 **Features:**
   Lists all transactions by date, type, category, and amount
   Shows income/expense totals
   Calculates current balance
   Uses data structures (lists, dicts, tuples) for organization

# 5. Exit
 **Function:** Terminates the application safely

# Data Structures Used

 **Lists:** `VALID_TRANSACTION_TYPES`, `CATEGORIES`, `MONTHS`, `transaction_list`
 **Dictionaries:** `summary` for income/expense totals
 **Tuples:** `transaction_tuple` for structured transaction data

# Database Schema

# Users Table
- `id` (Primary Key)
- `name` (String)
- `email` (String)

# Transactions Table
- `id` (Primary Key)
- `user_id` (Foreign Key)
- `amount` (Float)
- `category` (String)
- `type` (String: 'income' or 'expense')
- `date` (DateTime)

# Budgets Table
- `id` (Primary Key)
- `user_id` (Foreign Key)
- `category` (String)
- `limit` (Float)
- `month` (String)

# Testing

Run the test suite:
```bash
PYTHONPATH=. pipenv run pytest tests/ -v
```

## Project Structure
```
finance_tracker/
├── cli/
│   ├── __init__.py
│   └── main.py          # Main CLI logic with input validation
├── database/
│   ├── __init__.py
│   └── db.py            # SQLAlchemy engine and session
├── models/
│   ├── __init__.py
│   ├── user.py          # User model with relationships
│   ├── transaction.py   # Transaction model
│   └── budget.py        # Budget model
├── tests/
│   ├── __init__.py
│   ├── test_user.py     # User model tests
│   ├── test_transaction.py # Transaction model tests
│   ├── test_budget.py   # Budget model tests
│   ├── test_db.py       # Database tests
│   └── test_cli.py      # CLI tests
├── seed.py              # Database table creation
├── finance_tracker.db   # SQLite database (auto-generated)
├── Pipfile              # Dependencies
├── Pipfile.lock         # Locked dependencies
└── README.md            # This file
```

# Error Handling

The application includes comprehensive error handling:
- Input validation for all user inputs
- Database transaction rollbacks on errors
- Type conversion safety (prevents NaN injection)
- User-friendly error messages

# Learning Objectives Achieved

 **CLI Application:** Interactive command-line interface with menu system  
 **Object-Oriented Programming:** Models with relationships and methods  
 **SQLAlchemy ORM:** Database operations with 3+ related tables  
 **Data Structures:** Lists, dictionaries, and tuples throughout the application  
 **Input Validation:** Comprehensive validation and error handling  
 **Package Structure:** Proper Python package organization with `__init__.py` files  
 **Virtual Environment:** Pipenv for dependency management  
 **Testing:** Pytest test suite with fixtures and assertions