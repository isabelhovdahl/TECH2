# Exercise 3 — Temperature Conversion Function

def temp_conversion(temp, scale):
    """
    Convert a temperature between Fahrenheit and Celsius.

    Parameters
    ----------
    temp : float
        The temperature to convert.
    scale : str
        "F" to convert Fahrenheit to Celsius, or "C" to convert Celsius to
        Fahrenheit.

    Returns
    -------
    float
        The converted temperature.
    """
    if scale == "F":
        return (5 / 9) * (temp - 32)
    else:
        return (9 / 5) * temp + 32


if __name__ == "__main__":
    temp = 32
    scale = "F"

    converted = temp_conversion(temp, scale)
    print(f"{temp} degrees Fahrenheit is {converted:.1f} degrees Celsius.")
