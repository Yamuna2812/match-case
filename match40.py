num = int(input("Enter a number: "))

match True:
    case _ if num > 1 and all(num % i != 0 for i in range(2, num)):
        print("Prime Number")

    case _:
        print("Not a Prime Number")
