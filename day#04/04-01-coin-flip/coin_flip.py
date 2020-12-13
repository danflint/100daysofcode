""""
The flip coin program Heads or Tails. 
"""
from random import randint
import sys

print("Welcome in Heads or Tails!")
sample = 0
while True:
    key = input("If you want draw press enter or press q to exit")
    if key == 'q':
        sys.exit()
    else:
        sample += 1
        coin = randint(0, 1)
        if coin == 0:
            print(f"Sample {sample}: Head")
        else:
            print(f"Sample {sample}: Tail")
    

    