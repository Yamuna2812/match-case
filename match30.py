dept = input("Enter department: ")

match dept.lower():
    case "cse":
        print("Computer Science Department")

    case "ece":
        print("Electronics Department")

    case "me":
        print("Mechanical Department")

    case "civil":
        print("Civil Department")

    case _:
        print("Department not found")
