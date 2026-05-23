day = input("Enter day name: ")

match day.lower():
    case "saturday" | "sunday":
        print("Weekend")

    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("Weekday")

    case _:
        print("Invalid day")
