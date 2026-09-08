# Week 4 — Workshop Exercises

Before you start:

- Create a new folder for this week's workshop.
- Initialize a git repository inside it.
- Create a `.gitignore` file, copying its contents from [the standard template](../week02/gitignore-template.txt), then stage and commit it.

Solve each exercise in its own file: `ex1.py`, `ex2.py`, `ex3.py`, `ex4.py`. Commit your work after each one, whether it's finished or not.

---

## Before You Start

### Setting the random seed

The numbers produced by `random` aren't truly random. They're calculated from a starting value called the **seed**, which Python normally picks for you — which is why you get different numbers every time you run a program. If you set the seed yourself, you get the *same* sequence of "random" numbers every time:

```python
import random

random.seed(42)

print(random.randint(1, 100))
print(random.randint(1, 100))
```

This prints `82` and then `15`, no matter how many times you run it. Pick a different seed and you get a different pair of numbers — but again the same pair on every run.

> 📝 **Note:** Fixing the seed is useful whenever you need to reproduce a result: it lets you rewrite a piece of code and check that the output didn't change. It is not what you want in a program that should be genuinely unpredictable, like a lottery draw — there you leave the seed alone.

You'll need this for Exercise 1 below.

---

## Exercise 1 — Random Numbers

Modify the random number generator from last week (Exercise 1) to draw and summarize a whole sequence of random numbers:

- Set the random seed to `42` at the start of your program, so that you draw the same numbers every time you run it.
- Prompt the user for how many random numbers to draw (you can skip validating this input)
- Use a `for` loop and the `randint` function to draw that many random integers between 1 and 100, storing each one in a list
- Display the list of numbers drawn
- Display the **sum** and the **average** of the numbers, with the average rounded to **two decimals**
- Store the numbers **greater than 50** in a new list, and display that list along with how many numbers it contains

> 💡 **Tip:** Build both lists the way we did in the lecture — create an empty list, then `append` inside a `for` loop. If you finish early, have a look at the tip on *list comprehensions* at the bottom of this file, which does the same job in one line. Because you fixed the seed, you can swap one for the other and check that the numbers come out exactly the same.

---

## Exercise 2 — Prisoner's Dilemma (Take Two)

Modify the prisoner's dilemma program from last week (Exercise 2) so that instead of only checking the inputs once, the program keeps re-prompting each prisoner until they enter a valid choice:

- Prompt prisoner A for their choice, e.g. press "1" to confess or "2" to stay silent
- Keep re-prompting prisoner A until a valid choice ("1" or "2") is entered
- Do the same for prisoner B
- Display what each prisoner chose

You don't need to display the outcome (prison sentence) this time — that was last week's focus. This week is about the loop, not the payoff table.

> 💡 **Tip:** There are three ways to write this, all shown in the lecture: a `while` loop with a condition, a `while` loop controlled by a boolean flag, or `while True` with a `break`. Pick whichever one you find clearest, and try a second one if you finish early.

**Extra:** Wrap the whole game in an outer `while` loop so the prisoners can play multiple rounds, stopping only once they choose to quit (e.g., by answering "no" when asked if they want to play again).

---

## Exercise 3 — Phonebook

Write a program that builds a phonebook of names and phone numbers as the user enters them:

- Create an empty dictionary to store the phonebook
- Use a `while` loop to repeatedly prompt the user for a name and a phone number, adding each pair to the dictionary
- Stop the loop when the user enters an empty name (i.e., just presses enter)
- Use a `for` loop to display the final phonebook, one entry per line

> 💡 **Tip:** To display both the name and the phone number, loop over `phonebook.items()`. Each item is a tuple, so you can unpack it into two loop variables directly in the `for` header — `for name, number in phonebook.items():` — instead of looking each value up by its key.

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

**Extra:** Use `while` loops together with `try`/`except` to make sure the user-supplied inputs are valid numbers. Also make sure the inputs you accept guarantee the loop actually terminates — think about which of the three inputs must be **strictly positive** for the savings to ever reach the target.

---

## 💡 Tip — List Comprehensions

A **list comprehension** builds a list from a loop in a single line, instead of creating an empty list and calling `append` inside a `for` loop. Both lists you built in Exercise 1 can be written this way.

Drawing the numbers:

```python
numbers = [random.randint(1, 100) for i in range(count)]
```

which does the same as:

```python
numbers = []
for i in range(count):
    numbers.append(random.randint(1, 100))
```

A comprehension can filter as well, by ending it with an `if`:

```python
high_numbers = [num for num in numbers if num > 50]
```

which does the same as:

```python
high_numbers = []
for num in numbers:
    if num > 50:
        high_numbers.append(num)
```

Try it: replace the loops in your `ex1.py` with the one-line versions and run the script again. Since the seed is set at the top, the numbers are drawn from the same starting point every run, so the output should be identical down to the last digit — the two versions really are doing the same thing.

This isn't required to complete the exercises, and a `for` loop is never the wrong answer — but list comprehensions are common enough in real Python code that it's worth being able to read one. 
