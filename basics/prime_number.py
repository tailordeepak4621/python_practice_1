print("Enter the number to chack prime or not")
no = int(input("Enter number :"))
if no<2:
  print(" number is not prime ")
else:  
  for i in range(2,(no-1)):
     if no%i == 0:
      print(f"The number {no} is not prime.")   
      break         
  else:
      print("The number is  prime.") 