# sum_of_digits.py
# Task: Write a function to sum the digits of a given number.

# My Plan:
# 1. Create a function named sum_of_digits that accepts a number as a parameter.
# 2. Initialize a variable to store the total sum of the digits.
# 3. Use a loop to extract and sum the digits of the number.
# 4. Return the total sum.

# Writing the function

def sum_of_digits(number):
    # Initialize the sum of digits to 0
    total_sum = 0

    #convert number to its absolute value to handle negative numbers
    number = abs(number)


    # Loop through the number until it becomes 0
    while number > 0:
        # Extract the last digit using modulus operator
        digit = number % 10
        
        # Add the digit to the total sum
        total_sum += digit
        
        # Remove the last digit by performing integer division
        number //= 10

    # Return the total sum of digits
    return total_sum

# Testing the function

# Example number to test
test_number = 123456

print(f"The sum of the digits of {test_number} is {sum_of_digits(test_number)}")
