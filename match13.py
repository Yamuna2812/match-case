fruit = input("Enter fruit name: ")

match fruit.lower():
    case "apple":
        print("Price = 120")

    case "banana":
        print("Price = 40")

    case "mango":
        print("Price = 100")

    case _:
        print("Fruit not available")
