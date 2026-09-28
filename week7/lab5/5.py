balance = 1000

def deposit(amount):
    global balance
    balance = balance + amount
    print("Amount deposited:", amount)

def withdraw(amount):
    global balance

    if amount <= balance:
        balance = balance - amount
        print("Amount withdrawn:", amount)
    else:
        print("Insufficient funds")

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        deposit(amount)

    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        withdraw(amount)

    elif choice == 3:
        print("Current Balance:", balance)

    elif choice == 4:
        print("Thank you")
        break

    else:
        print("Invalid choice")