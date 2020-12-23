"""
The program adds evens numbers from range typed by user.
"""

print("Count evens numbers from x to y")
x = input("Input x value:\n")
y = input("Input y value:\n")

summary = 0
for num in range(int(x), int(y)+1):
    if num % 2 == 0:
        summary += num

print(f"Result of adding evens number is {summary}.")