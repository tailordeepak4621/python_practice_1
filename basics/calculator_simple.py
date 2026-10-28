# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y == 0:
#         return "Error! Division by zero."
#     return x / y

# def calculator():
#     print("--- Simple Python Calculator ---")
#     print("Select operation:")
#     print("1. Add (+)")
#     print("2. Subtract (-)")
#     print("3. Multiply (*)")
#     print("4. Divide (/)")
#     print("5. Exit")

#     while True:
#         choice = input("\nEnter choice (1/2/3/4/5): ").strip()

#         if choice == '5':
#             print("Goodbye!")
#             break

#         if choice in ('1', '2', '3', '4'):
#             try:
#                 num1 = float(input("Enter first number: "))
#                 num2 = float(input("Enter second number: "))
#             except ValueError:
#                 print("Invalid input! Please enter numbers only.")
#                 continue

#             if choice == '1':
#                 print(f"Result: {num1} + {num2} = {add(num1, num2)}")
#             elif choice == '2':
#                 print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
#             elif choice == '3':
#                 print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
#             elif choice == '4':
#                 print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
#         else:
#             print("Invalid choice! Please select a valid option (1-5).")

# if __name__ == "__main__":
#     calculator()
import math

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error! Division by zero." if y == 0 else x / y
def power(x, y): return x ** y
def percentage(x, y): return (x * y) / 100

def calculator():
    print("--- Advanced Python Calculator ---")
    current_result = None

    while True:
        # Step 1: Handle the first number / memory
        if current_result is not None:
            print(f"\n[ Memory: {current_result} ]")
            use_memory = input("Use memory as first number? (y/n) or type 'c' to clear: ").strip().lower()
            if use_memory == 'c':
                current_result = None
                print("Memory cleared.")
                continue
            elif use_memory == 'y':
                num1 = current_result
            else:
                current_result = None
                try:
                    num1 = float(input("Enter first number: "))
                except ValueError:
                    print("Invalid input! Numbers only.")
                    continue
        else:
            try:
                num1 = float(input("\nEnter first number: "))
            except ValueError:
                print("Invalid input! Numbers only.")
                continue

        # Step 2: Choose Operation
        print("\nOperations:")
        print(" +  : Add         |  -  : Subtract   |  *  : Multiply")
        print(" /  : Divide      |  ^  : Power      |  %  : Percentage of")
        print(" sq : Square Root |  x  : Clear/Exit")
        
        choice = input("Choose operation: ").strip().lower()

        if choice == 'x':
            print("Goodbye!")
            break
            
        # Handle single-input operation
        if choice == 'sq':
            if num1 < 0:
                print("Error! Cannot take square root of a negative number.")
                current_result = None
            else:
                current_result = math.sqrt(num1)
                print(f"Result: √{num1} = {current_result}")
            continue

        # Handle double-input operations
        if choice in ('+', '-', '*', '/', '^', '%'):
            try:
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Numbers only.")
                continue

            if choice == '+':
                current_result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {current_result}")
            elif choice == '-':
                current_result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {current_result}")
            elif choice == '*':
                current_result = multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {current_result}")
            elif choice == '/':
                res = divide(num1, num2)
                if isinstance(res, str):
                    print(res)
                    current_result = None
                else:
                    current_result = res
                    print(f"Result: {num1} / {num2} = {current_result}")
            elif choice == '^':
                current_result = power(num1, num2)
                print(f"Result: {num1} ^ {num2} = {current_result}")
            elif choice == '%':
                current_result = percentage(num1, num2)
                print(f"Result: {num2}% of {num1} = {current_result}")
        else:
            print("Invalid operation selected.")

if __name__ == "__main__":
    calculator()
