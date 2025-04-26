from account.user import User
from account.bank_account import BankAccount, SavingsAccount, CurrentAccount, StudentAccount

# users = []
users = [User('myo', 'a@a.a'), User('myo2', 'a2@a.a')]

def create_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    user = User(name, email)
    if not user.is_valid_email(email):
        print("Invalid email address!")
        return
    users.append(user)
    print(f"User {name} created.\n")

def list_users():
    if not users:
        print("No users.")
        return
    for i, user in enumerate(users):
        print(f"{i+1}. {user}") # Fixed (hope so)

def create_account():
    # Check if any users are available.
    if not users:
        print("No users available. Please create a user first.\n")
        return

    # List users (assumes list_users() prints each user with a number)
    list_users()
    
    # Get the selected user index with error handling and adjust for 0-based index.
    try:
        idx = int(input("Select user number: ")) - 1
    except ValueError:
        print("Invalid input for user selection!\n")
        return

    if idx < 0 or idx >= len(users):
        print("Invalid user selection.\n")
        return

    # Display account type choices.
    print("Account Type:")
    print("1. Savings Account")
    print("2. Students Account")
    print("3. Current Account")
    
    # Get account type choice with error handling.
    try:
        account_choice = int(input("Enter your choice (1, 2, 3): "))
    except ValueError:
        print("Invalid input for account type!")
        return

    # Get initial deposit amount with error handling.
    try:
        amount = float(input("Enter initial deposit: "))
    except ValueError:
        print("Invalid deposit amount!")
        return

    if amount < 0:
        print("Initial deposit cannot be negative!")
        return

    # Retrieve the selected user.
    selected_user = users[idx]

    # Create the account using the user’s details.
    if account_choice == 1:
        account = SavingsAccount(selected_user.name, selected_user.email, amount)
    elif account_choice == 2:
        account = StudentAccount(selected_user.name, selected_user.email, amount)
    elif account_choice == 3:
        account = CurrentAccount(selected_user.name, selected_user.email, amount)
    else:
        print("Invalid choice!")
        return

    # Add the account to the selected user's account list.
    selected_user.add_account(account)
    print(f"{account.get_account_type()} added for {selected_user.name}!\n")


def deposit_money():
    list_users()
    idx = int(input("Select user: ")) - 1
    user = users[idx]
    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. Balance: Rs. {acc.get_balance()}")
    acc_idx = int(input("Select account: ")) - 1
    amount = float(input("Enter amount to deposit: "))  # Fixed bug
    user.accounts[acc_idx].deposit(amount)

def withdraw_money():
    list_users()
    userid = int(input("Select user: ")) - 1
    user = users[userid]
    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. Balance: Rs. {acc.get_balance()}")
    acc_idx = int(input("Select account: ")) - 1
    amount = float(input("Enter amount to withdraw: "))
    try:
        user.accounts[acc_idx].withdraw(amount)
        print("Withdrawal successful.\n")
    except ValueError as e:
        print(f"Error: {e}\n")

def view_transactions():
    list_users()
    idx = int(input("Select user: ")) - 1
    user = users[idx]
    for i, acc in enumerate(user.accounts):
        print(f"\n{acc.get_account_type()} {i+1} - Balance: Rs. {acc.get_balance()}")
        for tx in acc.get_transaction_history():
            print(tx)

