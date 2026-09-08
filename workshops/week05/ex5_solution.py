# Exercise 4 — Temperature Conversion Program

# Note: this import only works if the file being imported from is in the same
# folder as this file, and your working directory is set to that folder. In
# your own solution that file is called "ex4.py", so your import would read
# "from ex4 import temp_conversion".
from ex4_solution import temp_conversion


# Note: get_temp and get_scale below solve the same problem - keep asking until
# the input is valid - but they leave the loop in two different ways. Compare
# them; both are correct.


def get_temp():
    """
    Prompt the user for a temperature to convert, making sure it's a valid number.

    Returns
    -------
    float
        The temperature to convert.
    """
    # Return from inside the loop: "return" leaves the loop AND the function in
    # one go, so a successful conversion ends the whole thing immediately. The
    # loop has no other way out, so this function cannot return anything but a
    # number.
    while True:
        try:
            return float(input("Enter the temperature to convert: "))
        except:
            print("Invalid input! Enter a number.")


def get_scale():
    """
    Prompt the user for the scale to convert from, re-prompting until valid.

    Returns
    -------
    str
        "F" or "C".
    """
    # The other way round: "break" leaves the loop only, and the function
    # returns afterwards. That costs an extra variable and an extra line, but it
    # keeps the return value in one obvious place at the end.
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
