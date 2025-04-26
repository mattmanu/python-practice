# sum_list.py
# Task: Write a function to sum all elements in a list.

# My Plan:
# 1. Create a function named sum_list that accepts a list as a parameter.
# 2. Initialize a variable (like total = 0) to keep track of the sum.
# 3. Loop through each element in the list.
# 4. Add each element to the total variable.
# 5. After the loop, return the total.

# Writing the function

def sum_list(numbers):
    # Initialize total
    total = 0

    # Loop through each number in the list
    for num in numbers:
        total += num  # Add the number to total

    # Return the final sum
    return total

# Testing the function

# Example list to test
test_numbers = [1, 2, 3, 4, 5]

# Call the function and print the result
print("Sum of list:", sum_list(test_numbers))
