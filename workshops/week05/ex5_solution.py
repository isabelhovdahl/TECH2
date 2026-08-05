# Exercise 4 — Temperature Conversion Program

# Note: this import only works if "ex4.py" is in the same folder as this
# file, and your working directory is set to that folder.
from ex4_solution import temp_conversion


def get_temp():
    """
    Prompt the user for a temperature to convert, making sure it's a valid number.

    Returns
    -------
    float
        The temperature to convert.
    """
    while True:
        try:
            temp = float(input("Enter the temperature to convert: "))
            break
        except:
            print("Invalid input! Enter a number.")

    return temp


def get_scale():
    """
    Prompt the user for the scale to convert from, re-prompting until valid.

    Returns
    -------
    str
        "F" or "C".
    """
    while True:
        scale = input("Convert from (F)ahrenheit or (C)elsius?: ").upper()
        if scale in ("F", "C"):
            break
        print('Invalid input! Enter "F" or "C".')

    return scale


def main():
    """Run the temperature conversion program."""
    print("Welcome to the Temperature Conversion Program.\n")

    scale = get_scale()
    temp = get_temp()

    converted = temp_conversion(temp, scale)

    if scale == "F":
        print(f"\n{temp} degrees Fahrenheit is {converted:.1f} degrees Celsius.")
    else:
        print(f"\n{temp} degrees Celsius is {converted:.1f} degrees Fahrenheit.")


if __name__ == "__main__":
    main()
