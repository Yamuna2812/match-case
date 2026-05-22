signal = input("Enter signal color: ")

match signal.lower():
    case "red":
        print("Stop")

    case "yellow":
        print("Ready")

    case "green":
        print("Go")

    case _:
        print("Invalid signal")
