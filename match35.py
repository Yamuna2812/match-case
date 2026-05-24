print("1. INR to USD")
print("2. USD to INR")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        inr = float(input("Enter INR: "))
        print("USD =", inr / 83)

    case 2:
        usd = float(input("Enter USD: "))
        print("INR =", usd * 83)

    case _:
        print("Invalid choice")
