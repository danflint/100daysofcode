"""
The program draws a word from list. 
User type a letter and program checks letter in word.
"""
import random

word_list = [
    'penguin', 'color', 'computer', 'prejudice', 'treasury', 'lobster',
    'weekend', 'dice', 'preproccessor',
    ]


chosen_word = word_list[random.randint(0, len(word_list) - 1)]

guess_field = ["_" for i in range(len(chosen_word) -1)]
guess = input("Guess a letter in secred word, type a letter and press enter.\n").lower()
 

for  i, letter in enumerate(chosen_word):
    if letter == guess:
        guess_field.insert(i, letter)

user_typed = ' '    
for letter in guess_field:
    user_typed += " " + letter

print(user_typed)