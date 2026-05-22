time=float(input("Enter time"))

match time:
    case 9:
        print("Breakfast time")
        
    case 13:
        print("Lunch time")
    
    case 16:
        print("Snacks time") 
        
    case 15:
        print("Dinner time")

    case _:
        print("working time")           