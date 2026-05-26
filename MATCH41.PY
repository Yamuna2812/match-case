year = int(input("Enter year: "))

match True:
    case _ if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("Leap Year")

    case _:
        print("Not a Leap Year")
