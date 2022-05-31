# leap year code 

year = int(input("whats the year you need to be cheaked?"))

if year % 4 == 0:
   
    if year % 100 == 0:
        
        if year % 400 ==0:
            print("leap year")
        else:
            print("not leap year.")
else:
    print("not leap year")
