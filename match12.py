print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice = int(input("Enter choice: "))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

match choice:
    case 1:
        print("Sum =", a + b)

    case 2:
        print("Difference =", a - b)

    case 3:
        print("Product =", a * b)

    case 4:
        if b != 0:
            print("Division =", a / b)
        else:
            print("Cannot divide by zero")

    case _:
        print("Invalid choice")
