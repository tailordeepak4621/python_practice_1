print("Enter a number :")
no = int(input("Enter number:"))

for i in range(1,no+1):
    for j in range(i):
        print("*",end="")
    print()    


for i in range(1,no+1):
    print("*"*i)
        