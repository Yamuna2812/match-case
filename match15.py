print("1. Circle")
print("2. Rectangle")
print("3. Square")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        r = float(input("Enter radius: "))
        print("Area =", 3.14 * r * r)

    case 2:
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        print("Area =", l * b)

    case 3:
        s = float(input("Enter side: "))
        print("Area =", s * s)

    case _:
        print("Invalid choice")
