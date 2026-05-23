print("1. Home")
print("2. Shop")
print("3. Factory")

choice = int(input("Enter connection type: "))

units = int(input("Enter units used: "))

match choice:
    case 1:
        print("Bill =", units * 5)

    case 2:
        print("Bill =", units * 8)

    case 3:
        print("Bill =", units * 10)

    case _:
        print("Invalid choice")
