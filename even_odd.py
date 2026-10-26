print("Enter a number for chacking the number is odd or even :")
no = int(input("Number is :"))

if no%2 == 0:
    if no > 0:
     print(" The number is (even) and (positive).")
    elif no == 0:
     print(" The number is (even) and (zero).")   
    else:
     print(" The number is (even) and (Negative).")
else:
       
     if no > 0:
         print(" The number is (odd) and (positive).")
     else:
         print(" The number is (odd) and (Negative).")
