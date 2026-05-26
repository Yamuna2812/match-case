print("1. Pizza")
print("2. Burger")
print("3. Pasta")

choice = int(input("Enter order number: "))

match choice:
    case 1:
        print("Pizza ordered")

    case 2:
        print("Burger ordered")

    case 3:
        print("Pasta ordered")

    case _:
        print("Invalid order")
