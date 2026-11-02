# Day 1 Solution
def check_even_odd():
    try:
        user_input = int(input("Enter an integer: "))
        # Evaluate absolute value to handle negative inputs safely
        number = abs(user_input)
        
        if number % 2 == 0:
            print(f"{user_input} is an Even number.")
        else:
            print(f"{user_input} is an Odd number.")
            
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    check_even_odd()
