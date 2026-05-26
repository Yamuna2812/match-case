answer = input("What is the capital of India? ")

match answer.lower():
    case "delhi":
        print("Correct Answer")

    case _:
        print("Wrong Answer")
