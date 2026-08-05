# Exercise 2 — Divide Two Floats

# Welcome message
print("This program divides two floating point values.\n")

# Prompt user for input and convert to float
num1 = float(input("Enter the first float: "))
num2 = float(input("Enter the second float: "))

# Store division in new variable
res = num1 / num2

# Display result with two decimals
print(f"{num1} / {num2} = {res:.2f}")

# Alternatively, pass the calculation directly to the f-string
#print(f"{num1} / {num2} = {num1 / num2:.2f}")