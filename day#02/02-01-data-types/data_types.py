"""
Write a program that adds the digits in a 2 digit number.
e.g. If the input was 45, then the output should be 4+5=9
"""

print("The program adds two digits. e.g \nIf you type 12 then your result would be 3")
input_number = input("Type a two digit number\n")
print(f"{input_number[0]} + {input_number[1]} = {int(input_number[0]) + int(input_number[1])}")
