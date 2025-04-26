# factorial_loop.py
# Task: Write a function to compute factorial using a loop.

# My Plan:
# 1. Create a function named factorial_loop that accepts one number as a parameter.
# 2. Initialize a result variable (like result = 1).
# 3. Use a for loop to multiply result by each number from 1 up to the given number.
# 4. After the loop ends, return the result.

# Writing the function

def factorial_loop(number):
    # Initialize result
    result = 1

    # Loop from 1 to number (inclusive)
    for i in range(1, number + 1):
        result *= i  # Multiply result by i

    # Return the factorial
    return result

# Testing the function

# Example numbers to test
test_number = 5

print(f"Factorial of {test_number} is", factorial_loop(test_number))
