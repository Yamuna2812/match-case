brand = input("Enter laptop brand: ")

match brand.lower():
    case "hp":
        print("HP selected")

    case "dell":
        print("Dell selected")

    case "lenovo":
        print("Lenovo selected")

    case "asus":
        print("Asus selected")

    case _:
        print("Brand not available")
