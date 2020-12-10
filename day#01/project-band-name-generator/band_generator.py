# Greeting the user
# Ask the user for the street/city that they grew up in.
# Ask the user for the name of a pet.
# Combine the name of their city and pet and show them their band name

#greetings
print("Hello,"  + input("What is your name?\n") + "!")

street = input("What is the name of street/city where you grew up?\n")
pet = input("What is your pet name?\n")

print(f"Your band name could be {street} {pet}.")
