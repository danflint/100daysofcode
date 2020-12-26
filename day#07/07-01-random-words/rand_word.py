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
guess = input("Guess a letter in secred word, type a letter and press enter.\n").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
