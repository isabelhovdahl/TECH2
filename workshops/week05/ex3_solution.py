# Exercise 2 — Random Code Generator

from random import randint


def random_character(characters):
    """
    Return a single random character from a sequence of characters.

    Parameters
    ----------
    characters : str
        The sequence to draw a character from.

    Returns
    -------
    str
        A random character from the sequence, or an empty string if the
        sequence is empty.
    """
    if len(characters) == 0:
        print("Warning: the sequence is empty.")
        return ""

    i = randint(0, len(characters) - 1)
    return characters[i]


#%% Alternative 1: for loop with string concatenation

code_length = 4
digits = "0123456789"

code = ""
for i in range(code_length):
    code = code + random_character(digits)

print(f"Your code is: {code}")


#%% Alternative 2: list comprehension and join

code_length = 8
letters = "abcdefghijklmnopqrstuvwxyz"

code_lst = [random_character(letters) for i in range(code_length)]
code = "".join(code_lst)  # join concatenates all characters in the list into one string

print(f"Your code is: {code}")
