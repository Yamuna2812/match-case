ch = input("Enter a letter: ")

match ch.lower():
    case "a" | "e" | "i" | "o" | "u":
        print("Vowel")

    case _:
        print("Consonant")
