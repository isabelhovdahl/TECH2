# Exercise 2 — Prisoner's Dilemma (Take Two)

#%% Alternative 1: while loop with a negated condition

# Dict that maps a choice to its label
choices = {
    "1": "confess",
    "2": "stay silent"
}

# Print welcome message
print("Welcome to the Prisoner's Dilemma.\n")

# Prompt prisoner A for their choice, re-prompting until valid
choice_a = input('Prisoner A, press "1" to confess or "2" to stay silent: ')
while choice_a not in choices:
    print("Invalid input. Try again.")
    choice_a = input('Prisoner A, press "1" to confess or "2" to stay silent: ')

# Prompt prisoner B for their choice, re-prompting until valid
choice_b = input('Prisoner B, press "1" to confess or "2" to stay silent: ')
while choice_b not in choices:
    print("Invalid input. Try again.")
    choice_b = input('Prisoner B, press "1" to confess or "2" to stay silent: ')

# Display each prisoner's choice
print(f"\nPrisoner A chose to {choices[choice_a]}.")
print(f"Prisoner B chose to {choices[choice_b]}.")


#%% Alternative 2: boolean flag

# Dict that maps a choice to its label
choices = {
    "1": "confess",
    "2": "stay silent"
}

# Print welcome message
print("Welcome to the Prisoner's Dilemma.\n")

# Prompt prisoner A for their choice, using a flag to track validity
valid_input = False
while not valid_input:
    choice_a = input('Prisoner A, press "1" to confess or "2" to stay silent: ')
    if choice_a in choices:
        valid_input = True
    else:
        print("Invalid input. Try again.")

# Prompt prisoner B for their choice, using a flag to track validity
valid_input = False
while not valid_input:
    choice_b = input('Prisoner B, press "1" to confess or "2" to stay silent: ')
    if choice_b in choices:
        valid_input = True
    else:
        print("Invalid input. Try again.")

# Display each prisoner's choice
print(f"\nPrisoner A chose to {choices[choice_a]}.")
print(f"Prisoner B chose to {choices[choice_b]}.")


#%% Alternative 3: while True with break

# Dict that maps a choice to its label
choices = {
    "1": "confess",
    "2": "stay silent"
}

# Print welcome message
print("Welcome to the Prisoner's Dilemma.\n")

# Prompt prisoner A for their choice, breaking out once valid
while True:
    choice_a = input('Prisoner A, press "1" to confess or "2" to stay silent: ')
    if choice_a in choices:
        break
    print("Invalid input. Try again.")

# Prompt prisoner B for their choice, breaking out once valid
while True:
    choice_b = input('Prisoner B, press "1" to confess or "2" to stay silent: ')
    if choice_b in choices:
        break
    print("Invalid input. Try again.")

# Display each prisoner's choice
print(f"\nPrisoner A chose to {choices[choice_a]}.")
print(f"Prisoner B chose to {choices[choice_b]}.")


#%% Extra: replay until the players want to quit

# Dict that maps a choice to its label
choices = {
    "1": "confess",
    "2": "stay silent"
}

# Print welcome message
print("Welcome to the Prisoner's Dilemma.\n")

# Keep playing rounds until the players want to quit
play_again = "yes"
while play_again == "yes":

    # Prompt prisoner A for their choice, re-prompting until valid
    choice_a = input('Prisoner A, press "1" to confess or "2" to stay silent: ')
    while choice_a not in choices:
        print("Invalid input. Try again.")
        choice_a = input('Prisoner A, press "1" to confess or "2" to stay silent: ')

    # Prompt prisoner B for their choice, re-prompting until valid
    choice_b = input('Prisoner B, press "1" to confess or "2" to stay silent: ')
    while choice_b not in choices:
        print("Invalid input. Try again.")
        choice_b = input('Prisoner B, press "1" to confess or "2" to stay silent: ')

    # Display each prisoner's choice
    print(f"\nPrisoner A chose to {choices[choice_a]}.")
    print(f"Prisoner B chose to {choices[choice_b]}.\n")

    # Ask whether to play another round
    play_again = input('Play again? ("yes"/"no"): ')

print("\nThanks for playing!")
