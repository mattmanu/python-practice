# factorial_recursive.py
# Task: Write a function to compute factorial using recursion.

# My Plan:
# 1. Create a function named factorial_recursive that accepts one number as a parameter.
# 2. Base Case: If the number is 0 or 1, return 1 (because 0! = 1 and 1! = 1).
# 3. Recursive Case: Multiply the number by factorial_recursive(number - 1).
# 4. Keep calling the function until it reaches the base case.

# Writing the function

def factorial_recursive(number):
    # Base case
    if number == 0 or number == 1:
        return 1
    else:
        # Recursive case
        return number * factorial_recursive(number - 1)

# Testing the function

# Example number to test
test_number = 6

print(f"Factorial of {test_number} is", factorial_recursive(test_number))
