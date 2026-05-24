age = int(input("Enter age: "))

match True:
    case _ if age < 5:
        print("Free Ticket")

    case _ if age <= 18:
        print("Ticket Price = 50")

    case _ if age <= 60:
        print("Ticket Price = 100")

    case _:
        print("Senior Citizen Ticket = 70")
