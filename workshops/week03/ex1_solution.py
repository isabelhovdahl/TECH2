# Exercise 1 — Random Number Generator with Input Validation

import random

#%% Alternative 1: nested if-else with isdigit

# Print welcome message
print("This program draws a random integer between a lower and upper bound.\n")

# Prompt user for lower and upper bounds
lower = input("Enter a lower bound: ")
upper = input("Enter an upper bound: ")

# Check that both bounds are integers
if lower.isdigit() and upper.isdigit():
    lower = int(lower)
    upper = int(upper)

    # Check that the bounds are valid
    if lower > upper:
        print("\nInvalid input!")
        print("The lower bound must be smaller than the upper bound.")
    else:
        # Draw and display random number
        rand_num = random.randint(lower, upper)
        print(f"\nYou asked for a random number between {lower} and {upper}.")
        print(f"Your random draw is... {rand_num}!")

# Print error message if bounds are not integers
else:
    print("\nInvalid input!")
    print("You can only enter non-negative integers.")


#%% Alternative 2: try-except

# Print welcome message
print("This program draws a random integer between a lower and upper bound.\n")

# Prompt user for lower and upper bounds
lower = input("Enter a lower bound: ")
upper = input("Enter an upper bound: ")

# Assume the inputs can be converted to integers
try:
    lower = int(lower)
    upper = int(upper)

    # Check that the bounds are valid
    if lower > upper:
        print("\nInvalid input!")
        print("The lower bound must be smaller than the upper bound.")
    else:
        # Draw and display random number
        rand_num = random.randint(lower, upper)
        print(f"\nYou asked for a random number between {lower} and {upper}.")
        print(f"Your random draw is... {rand_num}!")

# Print error message if the inputs could not be converted to integers
except:
    print("\nInvalid input!")
    print("You can only enter integers.")

# %%
