# Exercise 3 — Temperature Conversion (Fahrenheit <-> Celsius)

# Print welcome message
print("This program converts temperatures between Fahrenheit and Celsius.")
print('Press "F" to convert Fahrenheit to Celsius')
print('Press "C" to convert Celsius to Fahrenheit\n')

# Prompt user for conversion direction
direction = input("Enter selection: ").upper()

# Check that the selection is valid
if direction in ("F", "C"):
    temp = input("Enter the temperature to convert: ")

    # Check that the temperature is a valid number
    try:
        temp = float(temp)

        # Convert Fahrenheit -> Celsius
        if direction == "F":
            converted = (5 / 9) * (temp - 32)
            print(f"\n{temp} degrees Fahrenheit is {converted:.1f} degrees Celsius.")
        # Convert Celsius -> Fahrenheit
        else:
            converted = (9 / 5) * temp + 32
            print(f"\n{temp} degrees Celsius is {converted:.1f} degrees Fahrenheit.")

    # Print error message if temperature is not a valid number
    except:
        print("\nInvalid input!")
        print("The temperature must be a number.")

# Print error message if selection is invalid
else:
    print("\nInvalid input!")
    print('You can only select "F" or "C".')
