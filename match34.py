vehicle = input("Enter vehicle type: ")

match vehicle.lower():
    case "car":
        print("4 Wheeler")

    case "bike":
        print("2 Wheeler")

    case "bus":
        print("Public Transport")

    case "truck":
        print("Goods Vehicle")

    case _:
        print("Unknown Vehicle")
