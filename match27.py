print("1. Recharge 199")
print("2. Recharge 399")
print("3. Recharge 599")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("199 Recharge Successful")

    case 2:
        print("399 Recharge Successful")

    case 3:
        print("599 Recharge Successful")

    case _:
        print("Invalid choice")
