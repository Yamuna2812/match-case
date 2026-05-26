vehicle = input("Enter vehicle type: ")

match vehicle.lower():
    case "bike":
        print("Fine = 500")

    case "car":
        print("Fine = 1000")

    case "truck":
        print("Fine = 2000")

    case _:
        print("Invalid vehicle")
