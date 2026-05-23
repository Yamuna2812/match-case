word = input("Enter word: ")

match word.lower():
    case "hello":
        print("Kannada: Namaskara")

    case "thank you":
        print("Kannada: Dhanyavadagalu")

    case "water":
        print("Kannada: Neeru")

    case _:
        print("Word not found")
