no = int (input("Enter a number :"))

for i in range(0,no):
    if i==0 or i==no-1:
        print("* "*(no))
    else:
        print("  " + "  "+3*(no-2)* " " + "*" )    
