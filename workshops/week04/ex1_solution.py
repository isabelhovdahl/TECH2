# Exercise 1 — Random Numbers

import random

#%% Alternative 1: for loop with append

# Set the seed, so we draw the same numbers every time we run the program
random.seed(42)

# Print welcome message
print("This program draws a sequence of random numbers and summarizes them.\n")

# Prompt user for how many numbers to draw
count = int(input("How many random numbers do you want to draw? "))

# Draw random numbers and store them in a list
numbers = []
for i in range(count):
    numbers.append(random.randint(1, 100))

# Store the numbers greater than 50 in a new list
high_numbers = []
for num in numbers:
    if num > 50:
        high_numbers.append(num)

# Display the numbers, their sum and their average
print(f"\nNumbers drawn: {numbers}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / count:.2f}")

# Display the numbers greater than 50
print(f"\nNumbers greater than 50: {high_numbers}")
print(f"Count: {len(high_numbers)}")


#%% Alternative 2: list comprehension

# Set the seed again, so that this alternative starts from the same point as
# Alternative 1 above and draws exactly the same numbers. Enter the same count
# as before, and the output of the two alternatives should be identical.
random.seed(42)

# Print welcome message
print("This program draws a sequence of random numbers and summarizes them.\n")

# Prompt user for how many numbers to draw
count = int(input("How many random numbers do you want to draw? "))

# Draw random numbers using a list comprehension
numbers = [random.randint(1, 100) for i in range(count)]

# Store the numbers greater than 50 in a new list, filtering with an "if"
high_numbers = [num for num in numbers if num > 50]

# Display the numbers, their sum and their average
print(f"\nNumbers drawn: {numbers}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / count:.2f}")

# Display the numbers greater than 50
print(f"\nNumbers greater than 50: {high_numbers}")
print(f"Count: {len(high_numbers)}")
