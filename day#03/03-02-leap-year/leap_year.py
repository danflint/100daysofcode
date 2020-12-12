"""
    The program shows leap year.
    Conditionals if year/4 and year/400 -> leap year
"""

year = int(input("Which year do you want to check?"))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("It is a leap year.")
else:
    print("It is not a leap year.")