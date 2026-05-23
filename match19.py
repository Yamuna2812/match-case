password = input("Enter password: ")

match True:
    case _ if len(password) >= 8:
        print("Strong Password")

    case _:
        print("Weak Password")
