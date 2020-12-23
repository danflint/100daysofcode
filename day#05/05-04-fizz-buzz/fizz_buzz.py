"""
The game FizzBuzz. 
Start from 1 to 100.
Rules: if number is division by 3 say: 'Fizz',
       if number is division by 5 say: 'Buzz',
       if number is division by 15 say: 'FizzBuzz'.
"""
import time

for num in range(1, 101):
    time.sleep(0.09)
    if num % 3 == 0 and num % 5 != 0:
        print("Fizz")
    elif num % 5 == 0 and num % 3 != 0:
        print("Buzz")
    elif num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
    else:
        print(num)
