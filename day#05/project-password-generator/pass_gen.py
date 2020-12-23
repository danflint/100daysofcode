"""
PyPassword Generator.
Password can be created with letters, numbers and special symbols.
"""
from random import randint, shuffle

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*()_+}{'
letters_num = input("How many letters would you like in your passwrod?")
numbers_num = input("How many numbers would you like in your passwrod?")
symbols_num = input("How many special symbols would you like in your passwrod?")
password = []

for i in range(int(letters_num)):
    password.append(letters[randint(0, len(letters) - 1)])
for i in range(int(numbers_num)):
    password.append(numbers[randint(0, len(numbers) - 1)])
for i in range(int(symbols_num)):
    password.append(symbols[randint(0, len(symbols) - 1)])

shuffle(password)
pass_str = ''.join(str(sign) for sign in password)

print(f"Here is your password: {pass_str}")