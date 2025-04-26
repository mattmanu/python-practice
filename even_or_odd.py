# even_or_odd.py
# Task: Write a function to check if a number is even or odd.

# My Plan:
# 1. Create a function named check_even_odd that accepts one number as a parameter.
# 2. Use the modulo operator (%) to check if the number divided by 2 has a remainder.
#    - If number % 2 == 0, then it's even.
#    - Else, it's odd.
# 3. Return or print the result ("Even" or "Odd").

# Writing the function

def check_even_odd(number):
    # Check if number is divisible by 2
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Testing the function

# Example numbers to test
test_number_1 = 4
test_number_2 = 7

print(f"{test_number_1} is", check_even_odd(test_number_1))
print(f"{test_number_2} is", check_even_odd(test_number_2))
