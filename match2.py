age=int(input("enter age"))

match age:
    case _ if age< 5:
        print("free bus ticket")
        
    case _ if age > 60:
        print("senior citizen ticket")
        
    case _ if age>18 or age<59 :
        print("Adult! have to pay full amount")        

    case _:
        print("enter age 0<60<100")