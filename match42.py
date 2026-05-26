pin = int(input("Enter PIN: "))

match pin:
    case 1234:
        print("Login Successful")

    case _:
        print("Wrong PIN")
