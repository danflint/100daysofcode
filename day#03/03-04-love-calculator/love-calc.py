"""
The program calculates the chance at 'true love'. 
"""

name_1 = input("What is your name?\n")
name_2 = input("What is their name?\n")

both_names = name_1.lower() + name_2.lower()

dec_sum = both_names.count('t') + both_names.count('r') 
+ both_names.count('u') + both_names.count('e')
unity_sum = both_names.count('l') + both_names.count('o')
+ both_names.count('v') + both_names.count('e')

print(f"You chance at love is {dec_sum}{unity_sum}%.")