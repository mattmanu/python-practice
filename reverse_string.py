# reverse_string.py
# Task: Write a function to reverse a string (without using [::-1] or built-in methods).

# My Plan:
# 1. Create a function named reverse_string that accepts a string as a parameter.
# 2. Initialize an empty string to build the reversed string.
# 3. Use a loop to go through the original string from the last character to the first.
# 4. Add each character to the new string.
# 5. Return the reversed string.

# Writing the function

def reverse_string(text):
    # Initialize an empty string for the result
    reversed_text = ""

    # Loop through the original string backwards using a loop
    for i in range(len(text) - 1, -1, -1):
        reversed_text += text[i]  # Add each character from the end

    # Return the reversed string
    return reversed_text

# Testing the function

# Example text to test
test_text = "Emmanuel"

print(f"Reversed '{test_text}' is '{reverse_string(test_text)}'")
