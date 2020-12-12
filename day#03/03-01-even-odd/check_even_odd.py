""""
    The program check number and return even or odd.
"""

number = int(input("Which number do you want to check?"))

if not number == 0:
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
else:
    print("Number can't be 0.")