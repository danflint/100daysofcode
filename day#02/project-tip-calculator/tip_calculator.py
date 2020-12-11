""""
The tip bill calculator.
"""

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill?"))
tip_percentage = int(input("What percantege tip would you like to give? 10, 12 or 15?"))
people = int(input("How many people to split the bill?"))
bill_one_person = round(((total_bill + total_bill * (tip_percentage / 100)) / people), 2)

print(f"Each person should pay: {bill_one_person}")