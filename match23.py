weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height * height)

match True:
    case _ if bmi < 18.5:
        print("Underweight")

    case _ if bmi < 25:
        print("Normal Weight")

    case _ if bmi < 30:
        print("Overweight")

    case _:
        print("Obese")
