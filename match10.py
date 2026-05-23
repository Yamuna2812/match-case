print("1. Balance Check")
print("2. Withdraw")
print("3. Deposit")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Your balance is 5000")

    case 2:
        print("Withdrawal successful")

    case 3:
        print("Deposit successful")

    case _:
        print("Invalid choice")
