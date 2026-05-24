time = input("Enter time (morning/night): ")

match time.lower():
    case "morning":
        print("Wake up!")

    case "night":
        print("Go to sleep!")

    case _:
        print("Invalid time")
