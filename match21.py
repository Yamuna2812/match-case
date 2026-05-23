num = int(input("Enter number: "))

match num:
    case 1:
        print("Cricket")

    case 2:
        print("Football")

    case 3:
        print("Kabaddi")

    case 4:
        print("Hockey")

    case _:
        print("Invalid number")
