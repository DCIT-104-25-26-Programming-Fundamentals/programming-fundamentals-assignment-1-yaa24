# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def calculate_sum(numbers):
    
    total = 0
    for num in numbers:
        total += num
    return total

def calculate_average(numbers):
    total = calculate_sum(numbers)
    return total / len(numbers)

def find_maximum(numbers):
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

def find_minimum(numbers):
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

num_count = int(input("How many numbers? "))


if num_count <= 0:
    print("Error!! The count of numbers must be a positive integer.")
else:
    
    user_numbers = []
    
    
    for i in range(num_count):
        val = float(input(f"Enter number {i + 1}: "))
        user_numbers.append(val)
    
    
    total_sum = calculate_sum(user_numbers)
    average = calculate_average(user_numbers)
    maximum = find_maximum(user_numbers)
    minimum = find_minimum(user_numbers)
    
    
    print("\nResults:")
    print(f"Sum:     {total_sum}")
    print(f"Average: {average}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")
