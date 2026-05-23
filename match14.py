ch = input("Enter a character: ")

match True:
    case _ if ch.isalpha():
        print("Alphabet")

    case _ if ch.isdigit():
        print("Digit")

    case _:
        print("Special Character")
