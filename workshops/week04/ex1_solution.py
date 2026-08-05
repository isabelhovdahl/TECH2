# Exercise 1 — Random Numbers

import random

#%% Alternative 1: for loop with append

# Print welcome message
print("This program draws a sequence of random numbers and summarizes them.\n")

# Prompt user for how many numbers to draw
count = int(input("How many random numbers do you want to draw? "))

# Draw random numbers and store them in a list
numbers = []
for i in range(count):
    numbers.append(random.randint(1, 100))

# Display the numbers, their sum and their average
print(f"\nNumbers drawn: {numbers}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / count:.2f}")


#%% Alternative 2: list comprehension

# Print welcome message
print("This program draws a sequence of random numbers and summarizes them.\n")

# Prompt user for how many numbers to draw
count = int(input("How many random numbers do you want to draw? "))

# Draw random numbers using a list comprehension
numbers = [random.randint(1, 100) for i in range(count)]

# Display the numbers, their sum and their average
print(f"\nNumbers drawn: {numbers}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / count:.2f}")
