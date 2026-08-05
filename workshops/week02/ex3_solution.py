# Exercise 3 — Random Number Generator

import random

# Print welcome message
print("*"*49)
print("**** Welcome to the Random Number Generator! ****")
print("*"*49)
print("This program draws a random integer between an upper and lower bound.\n")

# Prompt user for upper and lower bounds
lower = int(input("Enter a lower bound: "))
upper = int(input("Enter an upper bound: "))

# Draw random number
rand_num = random.randint(lower, upper)
print(f"\nYou asked for a random number between {lower} and {upper}.")
print(f"Your random draw is... {rand_num}!")