# Week 3 — Workshop Exercises

Before you start:

- Create a new folder for this week's workshop.
- Initialize a git repository inside it.
- Create a `.gitignore` file, copying its contents from [the standard template](../week02/gitignore-template.txt), then stage and commit it.

Solve each exercise in its own file: `ex1.py`, `ex2.py`, `ex3.py`, `ex4.py`. Commit your work after each one, whether it's finished or not.

---

## Before You Start

### Handling invalid numeric input with `try`/`except`

When you convert user input to a number with `float()` or `int()`, Python raises an error and crashes the program if the input isn't actually a valid number. We can catch this with a `try`/`except` block instead of letting the program crash:

```python
try:
    num = float(input("Enter a number: "))
    print(f"You entered {num}")
except:
    print("That wasn't a valid number!")
```

Python first tries to run the code inside the `try` block. If an error occurs, it skips the rest of the `try` block and runs the `except` block instead.

---

## Exercise 1 — Random Number Generator with Input Validation

Modify the random number generator from last week (Exercise 3) to check that the user-supplied inputs are valid:

- Prompt the user for a lower and upper bound
- Check that both bounds are **integer** values (hint: `isdigit`)
- Check that the upper bound is **greater than** the lower bound
- If the inputs are invalid, display an error message instead of drawing a number
- Otherwise, draw and display the random number

> 💡 **Tip:** Build this up in stages — get the bound-checking working first (assuming the input is already a valid integer), then add the input validation around it once that part works.

---

## Exercise 2 — Prisoner's Dilemma

The prisoner's dilemma is a common example used in game theory. Two prisoners are interrogated separately and must each choose to stay silent (cooperate) or confess (defect):

| | Prisoner B stays silent | Prisoner B confesses |
|---|---|---|
| **Prisoner A stays silent** | Both serve 1 year | A: 3 years, B: goes free |
| **Prisoner A confesses** | A: goes free, B: 3 years | Both serve 2 years |

Write a program that:

- Prompts prisoner A and prisoner B for their choice, e.g. press "1" to confess or "2" to stay silent
- Checks that both inputs are valid (i.e., "1" or "2")
- Displays the outcome (prison sentence) for both prisoners

---

## Exercise 3 — Temperature Conversion (Fahrenheit ⇄ Celsius)

Modify the temperature conversion program from last week (Exercise 4) to let the user choose the direction of the conversion:

- Prompt the user to select a conversion direction, e.g. press "F" to convert Fahrenheit → Celsius, or "C" to convert Celsius → Fahrenheit
- Check that the selection is valid ("F" or "C")
- Prompt the user for the temperature to convert
- Use a `try`/`except` block to check that the temperature is a valid number (see *Before You Start*)
- Convert the temperature using the formulas:

  ```
  celsius = (5 / 9) * (fahrenheit - 32)
  fahrenheit = (9 / 5) * celsius + 32
  ```

- Display the converted temperature with **one decimal**

---

## Exercise 4 — Temperature Conversion (Fahrenheit, Celsius, Kelvin)

Extend the program from Exercise 3 to also support Kelvin:

- Prompt the user for i) a temperature, ii) the scale to convert **from** (F, C or K), and iii) the scale to convert **to** (F, C or K)
- For simplicity, you can skip validating the inputs this time
- Convert the temperature using the formulas:

  ```
  celsius = (5 / 9) * (fahrenheit - 32)
  fahrenheit = (9 / 5) * celsius + 32
  kelvin = celsius + 273.15
  celsius = kelvin - 273.15
  fahrenheit = (9 / 5) * (kelvin - 273.15) + 32
  kelvin = (fahrenheit - 32) * 5 / 9 + 273.15
  ```

- Display the conversion to the user, rounded to **one decimal**
