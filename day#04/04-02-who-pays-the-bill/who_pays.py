"""
Type the names and draw who pays the bill?
The rule is simple who has been chose chosen pay for all.
"""
from random import randint

participants_quantity = int(input("How many people play?\n"))
participants_lists  = []

for i in range(participants_quantity):
    participants_lists.append(input("Type the full name who is playing.\n"))

payer = participants_lists[randint(0, participants_quantity - 1)]

print(f"{payer.capitalize()} pays the bill.")
