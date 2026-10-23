# Basic Banking System in Python

account_balance = 1000.0


def deposit(amount):
    global account_balance
    if amount > 0:
        account_balance += amount
        print(f"Deposit successful. New balance: ${account_balance:.2f}")
    else:
        print("Deposit amount must be greater than 0.")


def withdraw(amount):
    global account_balance
    if amount > 0:
        if amount <= account_balance:
            account_balance -= amount
            print(f"Withdrawal successful. New balance: ${account_balance:.2f}")
        else:
            print("Insufficient balance.")
    else:
        print("Withdrawal amount must be greater than 0.")


def check_balance():
    print(f"Current balance: ${account_balance:.2f}")


while True:
    print("\nBanking System")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        deposit(amount)
    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        withdraw(amount)
    elif choice == "3":
        check_balance()
    elif choice == "4":
        print("Thank you for using the bank.")
        break
    else:
        print("Invalid option. Please try again.")
