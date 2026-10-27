no = int(input("Enter a number:"))

for i in range(1,no+1):
    for j in range(no-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")    
    print()    

  