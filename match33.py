category = input("Enter category: ")

match category.lower():
    case "student":
        print("50% Discount")

    case "senior citizen":
        print("40% Discount")

    case "disabled":
        print("60% Discount")

    case _:
        print("No Discount")
