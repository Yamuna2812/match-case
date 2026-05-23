msg = input("You: ")

match msg.lower():
    case "hi":
        print("Bot: Hello!")

    case "how are you":
        print("Bot: I am fine")

    case "bye":
        print("Bot: Goodbye")

    case _:
        print("Bot: I don't understand")
