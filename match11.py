username = input("Enter username: ")

match username:
    case "admin":
        print("Welcome Admin")

    case "student":
        print("Welcome Student")

    case "guest":
        print("Welcome Guest")

    case _:
        print("Unknown User")
