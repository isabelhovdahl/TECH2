# Week 5 — Workshop Exercises

Before you start:

- Create a new folder for this week's workshop.
- Initialize a git repository inside it.
- Create a `.gitignore` file, copying its contents from [the standard template](../week02/gitignore-template.txt), then stage and commit it.

Solve each exercise in its own file: `ex1.py`, `ex2.py`, `ex3.py`, `ex4.py`, `ex5.py`. Commit your work after each one, whether it's finished or not. Note that Exercise 1 spans two files (`ex1.py` and `ex2.py`) — see below.

---

## Before You Start

### Docstrings

A docstring is a short description of what a function does, written as a string literal right after the function header. It's good practice to document your functions this way, especially once other people (or your future self) need to reuse them.

```python
def square(num):
    """Return the square of a number."""
    return num**2
```

You'll use docstrings throughout this week's exercises. See the bottom of this file for instructions on how to auto-generate docstrings in VS Code.

### Running a script vs. importing from it

So far, every script we've written runs its code the moment it's executed. But once we start defining reusable functions, we often want to *import* a function from one script into another — without re-running the first script's demo/test code every time it's imported.

Python lets us guard code so that it only runs when the script is executed directly (not when it's imported), using:

```python
if __name__ == "__main__":
    <code that should only run when this file is executed directly>
```

When a script is *run*, Python sets its special variable `__name__` to `"__main__"`. When a script is instead *imported* from another file, `__name__` is set to the script's file name instead — so the code inside the `if` block is skipped.

> 📝 **Note:** For an import like `from ex1 import effective_interest_rate` to work, `ex1.py` must be in the same folder as the file importing it, and your working directory must be set to that folder.

You'll need this for Exercises 1 and 4 below.

---

## Exercise 1 — Effective Interest Rate

This exercise is borrowed from TECH1 (Examples 11.1.3 and 11.1.4).

**Part A (`ex1.py`):** Create a function called `effective_interest_rate` that calculates the effective annual interest rate:

- The function should have two parameters: `r` (the nominal annual interest rate) and `n` (the number of times per year the interest is compounded), with `n` defaulting to `12` (monthly compounding).
- Calculate the effective interest rate using the formula:

  ```
  R = (1 + r / n)**n - 1
  ```

- The function should **return** the result, and include a docstring.
- Guard your demonstration code (e.g. calculating the effective rate for a 9% annual rate compounded quarterly and monthly) with `if __name__ == "__main__":`, so it only runs when `ex1.py` is executed directly.

**Part B (`ex2.py`):** Import `effective_interest_rate` from `ex1.py`, and use it to compare two savings offers: (i) 5.9% compounded quarterly, or (ii) 6% compounded twice a year. Which offer is better?

---

## Exercise 2 — Random Code Generator

Write a program that generates a random code of a given length, built up one character at a time:

- Create a function called `random_character` that returns a single random character from a given sequence of characters (hint: use `randint` from `random` to draw a random index). Make sure the function handles the case where the sequence is empty.
- Use `random_character` inside a loop to build up a random code of a specified length, one character at a time.
- Display the generated code.

Demonstrate your program by generating a few different codes:
- a 4-digit PIN using the digits `"0123456789"`
- an 8-character code using the letters `"abcdefghijklmnopqrstuvwxyz"`

---

## Exercise 3 — Temperature Conversion Function

Turn the temperature-conversion logic from week 2 (Exercise 4) into a reusable function:

- Create a function called `temp_conversion` with two parameters: `temp` (the temperature to convert) and `scale` (`"F"` to convert Fahrenheit to Celsius, or `"C"` to convert Celsius to Fahrenheit).
- Convert the temperature using the formulas:

  ```
  celsius = (5 / 9) * (fahrenheit - 32)
  fahrenheit = (9 / 5) * celsius + 32
  ```

- The function should **return** the converted temperature (rather than printing it), and include a docstring.
- Guard your demonstration code with `if __name__ == "__main__":`, since you'll import this function in Exercise 4.

Demonstrate the function by converting 32 degrees Fahrenheit to Celsius.

---

## Exercise 4 — Temperature Conversion Program

Rebuild the temperature-conversion program using functions only, by combining what you've learned this week and in previous weeks:

- Import `temp_conversion` from `ex4.py` rather than redefining it.
- Write three more functions:
  - `get_temp` — prompts the user for the temperature to convert, making sure it's a valid number (hint: `try`/`except`, from week 3)
  - `get_scale` — prompts the user for the scale to convert from ("F" or "C"), re-prompting until a valid choice is entered (hint: a `while` loop, from week 4)
  - `main` — calls the other functions to run the whole program and displays the converted temperature
- Run the program by calling `main()`, guarded by `if __name__ == "__main__":`.

---

## 💡 Tip — Auto-Generating Docstrings

VS Code doesn't generate docstrings out of the box, but the **autoDocstring** extension does:

1. Install the extension **"autoDocstring - Python Docstring Generator"** (publisher: Nils Werner, id `njpwerner.autodocstring`) from the Extensions panel.
2. Open Settings (`Ctrl+,`), search for **autoDocstring**, and set **Docstring Format** to `numpy` — this matches the style used in this course's solution scripts.
3. To use it: on the line right after a function's `def` line, type `"""` and press **Enter**. It fills in a docstring template using the function's actual parameter names (and defaults), which you then fill in with descriptions.

This isn't required to complete the exercises — you can always type docstrings by hand — but it's a handy shortcut once you're writing functions with several parameters.
