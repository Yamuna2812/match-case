month = input("Enter month name: ")

match month.lower():
    case "march" | "april" | "may":
        print("Summer Season")

    case "june" | "july" | "august":
        print("Rainy Season")

    case "september" | "october" | "november":
        print("Autumn Season")

    case "december" | "january" | "february":
        print("Winter Season")

    case _:
        print("Invalid month")
