day=input("enter")

match day:
    case "Monday":
        print("Working day")
    
    case "Tuesday":
        print("Working day")
        
    case "Wednesday":
        print("mid workinf day")
        
    case "Thursday":
        print("working day")
        
    case "friday":
        print("almost weekend")
        
    case "saturday | sunday":
        print("Weekend")
        
    case _:
        print("invalid day.enter correct day")                      