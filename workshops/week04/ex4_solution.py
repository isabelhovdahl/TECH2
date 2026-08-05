# Exercise 4 — Savings Calculator

#%% Simple version (no input validation)

TARGET = 1_000_000

# Print welcome message
print("This program calculates how many years it takes to save 1 million NOK.\n")

# Prompt user for inputs
current = float(input("Enter your current savings (in NOK): "))
annual_savings = float(input("Enter how much you save each year (in NOK): "))
rate = float(input("Enter the annual interest rate (in %): "))

# Update savings each year until the target is reached
years = 0
while current < TARGET:
    current = (current + annual_savings) * (1 + rate / 100)
    years = years + 1

# Display the result
print(f"\nIt will take {years} years to save {TARGET:,} NOK.")


#%% Extra: validating the inputs

TARGET = 1_000_000

# Print welcome message
print("This program calculates how many years it takes to save 1 million NOK.\n")

# Prompt for and validate the current savings amount (must be positive, or the
# loop never gets started even with a positive interest rate)
while True:
    try:
        current = float(input("Enter your current savings (in NOK): "))
        if current <= 0:
            print("Please enter a positive number.")
        else:
            break
    except:
        print("Please enter a valid number.")

# Prompt for and validate the annual savings amount (must be non-negative)
while True:
    try:
        annual_savings = float(input("Enter how much you save each year (in NOK): "))
        if annual_savings < 0:
            print("Please enter a non-negative number.")
        else:
            break
    except:
        print("Please enter a valid number.")

# Prompt for and validate the annual interest rate (must be positive, or the
# savings never grow)
while True:
    try:
        rate = float(input("Enter the annual interest rate (in %): "))
        if rate <= 0:
            print("Please enter a positive number.")
        else:
            break
    except:
        print("Please enter a valid number.")

# Update savings each year until the target is reached
years = 0
while current < TARGET:
    current = (current + annual_savings) * (1 + rate / 100)
    years = years + 1

# Display the result
print(f"\nIt will take {years} years to save {TARGET:,} NOK.")
