print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        c = float(input("Enter Celsius: "))
        f = (c * 9/5) + 32
        print("Fahrenheit =", f)

    case 2:
        f = float(input("Enter Fahrenheit: "))
        c = (f - 32) * 5/9
        print("Celsius =", c)

    case _:
        print("Invalid choice")
