# Week 2 — Workshop Exercises

Solve each exercise in its own file: `ex1.py`, `ex2.py`, `ex3.py`, `ex4.py`. Commit your work after each one, whether it's finished or not.

Before your first commit, make sure you have followed the two setup steps from the slides: told git your name and email (`git config --global ...`), and created a `.gitignore` file in your week02 folder — copy its contents from [`gitignore-template.txt`](gitignore-template.txt).

---

## Before You Start

### Getting input from the user

Use the built-in `input()` function to ask the user to type something. It always returns a string, so if you need a number, convert it with `int()` or `float()`.

```python
name = input("What is your name? ")
age = int(input("How old are you? "))

print(name, age)
```

### Importing a package

Some tasks need functionality that isn't built into Python by default. To use it, `import` the package at the very top of your script — before anything else:

```python
import random

number = random.randint(1, 10)
print(number)
```

You'll need this for Exercise 3 below.

---

## Exercise 1 — Divide Two Integers

Write a program that divides two integers:

- Use `input()` to prompt the user for two **integer** values
- Divide the first number by the second number
- Display the result of the operation with **one decimal**

---

## Exercise 2 — Divide Two Floats

Write a program that divides two floats:

- Use `input()` to prompt the user for two **float** values
- Divide the first number by the second number
- Display the result of the operation with **two decimals**

---

## Exercise 3 — Random Number Generator

Write a program that draws a random number between a lower and upper bound:

- Use `input()` to prompt the user for a lower and upper bound
- Import the `random` package (see above)
- Use the `randint` function from `random` to draw a random integer between the   user-supplied bounds ([see the function documentation](https://docs.python.org/3/library/random.html#random.randint))
- Display the random number

---

## Exercise 4 — Fahrenheit to Celsius

Write a program that converts a temperature from Fahrenheit to Celsius:

- Use `input()` to prompt the user for a temperature in Fahrenheit
- Convert the temperature using the formula:

  ```
  celsius = (5 / 9) * (fahrenheit - 32)
  ```

- Display the converted temperature rounded to the **nearest integer**