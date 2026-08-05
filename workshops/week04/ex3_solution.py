# Exercise 3 — Phonebook

# Create an empty dictionary to store the phonebook
phonebook = {}

# Print welcome message
print("Let's build a phonebook. Press enter with no name to stop.\n")

# Keep prompting for entries until the user enters an empty name
while True:
    name = input("Enter a name: ")
    if name == "":
        break

    phone_number = input(f"Enter the phone number for {name}: ")
    phonebook[name] = phone_number
    print(f"Added {name} to the phonebook.\n")

# Display the final phonebook
print("\nFinal phonebook:")
for name, number in phonebook.items():
    print(f"{name}: {number}")
