# Week 4 — Workshop Exercises

Before you start:

- Create a new folder for this week's workshop.
- Initialize a git repository inside it.
- Create a `.gitignore` file, copying its contents from [the standard template](../week02/gitignore-template.txt), then stage and commit it.

Solve each exercise in its own file: `ex1.py`, `ex2.py`, `ex3.py`, `ex4.py`. Commit your work after each one, whether it's finished or not.

---

## Before You Start

### List comprehensions

A list comprehension lets you build a list from a loop in a single line, instead of creating an empty list and calling `append` inside a `for` loop:

```python
squares = [i**2 for i in range(5)]
print(squares)
```

This is equivalent to:

```python
squares = []
for i in range(5):
    squares.append(i**2)
```

You'll need this for Exercise 1 below.

---

## Exercise 1 — Random Numbers

Modify the random number generator from last week (Exercise 1) to draw and summarize a whole sequence of random numbers:

- Prompt the user for how many random numbers to draw (you can skip validating this input)
- Use a `for` loop and the `randint` function to draw that many random integers between 1 and 100, storing each one in a list
- Display the list of numbers drawn
- Display the **sum** and the **average** of the numbers, with the average rounded to **two decimals**

---

## Exercise 2 — Prisoner's Dilemma (Take Two)

Modify the prisoner's dilemma program from last week (Exercise 2) so that instead of only checking the inputs once, the program keeps re-prompting each prisoner until they enter a valid choice:

- Prompt prisoner A for their choice, e.g. press "1" to confess or "2" to stay silent
- Keep re-prompting prisoner A until a valid choice ("1" or "2") is entered
- Do the same for prisoner B
- Display what each prisoner chose

You don't need to display the outcome (prison sentence) this time — that was last week's focus. This week is about the loop, not the payoff table.

**Extra (optional):** Wrap the whole game in an outer `while` loop so the prisoners can play multiple rounds, stopping only once they choose to quit (e.g., by answering "no" when asked if they want to play again).

---

## Exercise 3 — Phonebook

Write a program that builds a phonebook of names and phone numbers as the user enters them:

- Create an empty dictionary to store the phonebook
- Use a `while` loop to repeatedly prompt the user for a name and a phone number, adding each pair to the dictionary
- Stop the loop when the user enters an empty name (i.e., just presses enter)
- Use a `for` loop to display the final phonebook, one entry per line

---

## Exercise 4 — Savings Calculator

Write a program that calculates how many years it will take to save 1 million NOK:

- Prompt the user for:
  - The current amount in their savings account (in NOK)
  - The amount they save each year (in NOK)
  - The annual interest rate (in percent)
- Use a `while` loop to update the current savings amount each year using the formula:

  ```
  current = (current + annual_savings) * (1 + rate / 100)
  ```

- Display the number of years it takes for the savings to reach (or exceed) 1 million NOK

**Extra (optional):** Use `while` loops together with `try`/`except` to make sure the user-supplied inputs are valid numbers. Also make sure the inputs you accept guarantee the loop actually terminates — think about which of the three inputs must be **strictly positive** for the savings to ever reach the target.
