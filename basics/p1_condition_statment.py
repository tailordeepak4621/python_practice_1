no1 = float(input("Enter a number :"))
no2 = float(input("Enter a number :"))



if no1 > 0 and no2 > 0:
    print("both numbers are positive ")
elif no1 > 0 and no2 < 0:
    print("no1 is positive but no2 is negative")    
elif no1 < 0 and no2 > 0:
    print("no1 is negative but no2 is positive")  
elif no1 == 0 and no2 == 0:
    print("Both are zero")         
else:
    print("Both are negative ")
