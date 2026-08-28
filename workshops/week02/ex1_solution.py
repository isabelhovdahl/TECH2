# Exercise 1 — Divide Two Integers

# Welcome message
print("This program divides two integer values.\n")

# Prompt user for input and convert to integer
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Store division in new variable
res = num1 / num2

# Display result with one decimal, using round() in a traditional print statement
#print(num1, "/", num2, "=", round(res, 1))

# Alternatively, use an f-string to insert the values and format the result directly
print(f"{num1} / {num2} = {res:.1f}")
