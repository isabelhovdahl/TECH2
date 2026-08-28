# Exercise 2 — Divide Two Floats

# Welcome message
print("This program divides two floating point values.\n")

# Prompt user for input and convert to float
num1 = float(input("Enter the first float: "))
num2 = float(input("Enter the second float: "))

# Store division in new variable
res = num1 / num2

# Display result with two decimals, using round() in a traditional print statement
#print(num1, "/", num2, "=", round(res, 2))

# Alternatively, use an f-string to insert the values and format the result directly
print(f"{num1} / {num2} = {res:.2f}")
