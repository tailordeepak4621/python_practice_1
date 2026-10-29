no = int (input("Enter a number :"))

for i in range(0,no):
    if i==0 or i==no-1:
        print("* "*no)
    else:
        print("  "+"*"+" "*(no-1)+"   *")   

print()
print()


for i in range(0,no):
    if i==0 or i==no-1 or i==((no%2)+1):
        print("* "*(no-1))
    else:
        print("*"+" "*(no-1))   

print()
print()


for i in range(0,no):
    if i==0 or i==no-1 or i==((no%2)+1):
        print("* "*(no-1))
    else:
        print("*"+" "*(no-1))


print()
print()


for i in range(0,no):
    if i==0 or i==((no%2)+1):
        print("* "*(no-2))
    elif i<no // 2:
        print("* "+ "  " * (no-4) + "*")    
    else:
        print("*")   


print()
print()


for i in range(0,no):
    if i==0 or i==((no%2)+1):
        print("* "*(no-2))
    else:
        print("*"+"   "+"*")           


print()
print()


for i in range(0,no):
    for j in range(0,no):
       if j==0 or (i+j == no //2) or (i-j==no //2):
           print("*",end=" ")
       else:
           print(" ", end=" ")
    print()       
              
