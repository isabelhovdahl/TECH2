# Exercise 4 — Temperature Conversion (Fahrenheit, Celsius, Kelvin)

# Dict that maps a scale letter to its full name
scales = {
    "F": "Fahrenheit",
    "C": "Celsius",
    "K": "Kelvin"
}

# Print welcome message
print("This program converts temperatures between Fahrenheit, Celsius and Kelvin.\n")

# Prompt user for temperature and convert to float
temp = float(input("Enter the temperature: "))

# Prompt user for the scale to convert from and to
from_scale = input("Convert from (F)ahrenheit, (C)elsius or (K)elvin?: ").upper()
to_scale = input("Convert to (F)ahrenheit, (C)elsius or (K)elvin?: ").upper()

# Converting from Fahrenheit...
if from_scale == "F":
    if to_scale == "C":
        converted = (5 / 9) * (temp - 32)
    elif to_scale == "K":
        converted = (temp - 32) * 5 / 9 + 273.15
    else:
        converted = temp

# Converting from Celsius...
elif from_scale == "C":
    if to_scale == "F":
        converted = (9 / 5) * temp + 32
    elif to_scale == "K":
        converted = temp + 273.15
    else:
        converted = temp

# Converting from Kelvin...
else:
    if to_scale == "F":
        converted = (9 / 5) * (temp - 273.15) + 32
    elif to_scale == "C":
        converted = temp - 273.15
    else:
        converted = temp

# Display the conversion
print(f"\n{temp:.1f} degrees {scales[from_scale]} is {converted:.1f} degrees {scales[to_scale]}.")
