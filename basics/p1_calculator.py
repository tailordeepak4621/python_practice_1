number_1 = float(input("Enter a  first number :"))
number_2 = float(input("Enter a  second number :"))

op = input("Enter a operator '+,-,*,/'")

if op == '+':
    print(f"sum of numbers : {number_1 + number_2}")
elif op == '-':
    print(f"difference of numbers : {number_1 - number_2}")
elif op == '*':
    print(f"multiply of numbers : {number_1 * number_2}")
elif op == '/':
    if number_2 != 0:
     print(f"devide of numbers : {number_1 / number_2}")    
    else:
       print("roung input!")