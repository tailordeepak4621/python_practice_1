print("Enter a number :")
no = int(input("Enter number:"))

for i in range(1,no+1):
    k=1
    for j in range(i):
        print(k,end="")
        k=k+1
    
    print()    
