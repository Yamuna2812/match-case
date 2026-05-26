animal = input("Enter animal name: ")

match animal.lower():
    case "dog":
        print("Bark")

    case "cat":
        print("Meow")

    case "cow":
        print("Moo")

    case "lion":
        print("Roar")

    case _:
        print("Unknown animal")
