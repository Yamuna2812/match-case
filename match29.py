num = int(input("Enter a number: "))

match num:
    case 2:
        for i in range(1, 11):
            print("2 x", i, "=", 2 * i)

    case 5:
        for i in range(1, 11):
            print("5 x", i, "=", 5 * i)

    case 10:
        for i in range(1, 11):
            print("10 x", i, "=", 10 * i)

    case _:
        print("Table not available")
