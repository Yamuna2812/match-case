balance = 5000

print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Balance =", balance)

    case 2:
        amount = int(input("Enter deposit amount: "))
        balance += amount
        print("New Balance =", balance)

    case 3:
        amount = int(input("Enter withdraw amount: "))
        if amount <= balance:
            balance -= amount
            print("Remaining Balance =", balance)
        else:
            print("Insufficient Balance")

    case _:
        print("Invalid choice")
