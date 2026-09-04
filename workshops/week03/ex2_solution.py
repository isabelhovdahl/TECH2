# Exercise 2 — Prisoner's Dilemma

#%% Alternative 1: nested if-else

# Dict that maps a choice to its label
choices = {
    "1": "confess",
    "2": "stay silent"
}

# Print welcome message
print("Welcome to the Prisoner's Dilemma.\n")

# Prompt prisoner A and B for their choice
choice_a = input('Prisoner A, press "1" to confess or "2" to stay silent: ')
choice_b = input('Prisoner B, press "1" to confess or "2" to stay silent: ')

# Check that both choices are valid
if choice_a in choices and choice_b in choices:
    print(f"\nPrisoner A chose to {choices[choice_a]} and prisoner B chose to {choices[choice_b]}.\n")

    # Nested if-else: first on prisoner A's choice, then on prisoner B's choice
    if choice_a == "1":
        if choice_b == "1":
            print("Both prisoners serve 2 years.")
        else:
            print("Prisoner A goes free, prisoner B serves 3 years.")
    else:
        if choice_b == "1":
            print("Prisoner A serves 3 years, prisoner B goes free.")
        else:
            print("Both prisoners serve 1 year.")

# Print error message if either choice is invalid
else:
    print("\nInvalid input!")
    print('You can only press "1" or "2".')


#%% Alternative 2: if-elif chain

# Dict that maps a choice to its label
choices = {
    "1": "confess",
    "2": "stay silent"
}

# Print welcome message
print("Welcome to the Prisoner's Dilemma.\n")

# Prompt prisoner A and B for their choice
choice_a = input('Prisoner A, press "1" to confess or "2" to stay silent: ')
choice_b = input('Prisoner B, press "1" to confess or "2" to stay silent: ')

# Check that both choices are valid
if choice_a in choices and choice_b in choices:
    print(f"\nPrisoner A chose to {choices[choice_a]} and prisoner B chose to {choices[choice_b]}.\n")

    # Both confess
    if choice_a == "1" and choice_b == "1":
        print("Both prisoners serve 2 years.")
    # A confesses, B stays silent
    elif choice_a == "1" and choice_b == "2":
        print("Prisoner A goes free, prisoner B serves 3 years.")
    # A stays silent, B confesses
    elif choice_a == "2" and choice_b == "1":
        print("Prisoner A serves 3 years, prisoner B goes free.")
    # Both stay silent
    else:
        print("Both prisoners serve 1 year.")

# Print error message if either choice is invalid
else:
    print("\nInvalid input!")
    print('You can only press "1" or "2".')

# %%
