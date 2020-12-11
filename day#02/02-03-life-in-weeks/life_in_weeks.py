"""
    Calculate how many time does user live in weeks.
    Calculate how many time to 90 years old user has left. View days, weeks and moth. 
"""

# actual age 
# age * 7
# you have x years , y moths, z day left.

user_age = int(input("What is your current age?"))
user_weeks_of_life = user_age * 52

print(f"You life is equal to {user_weeks_of_life} weeks.")

#left to 90 years old
weeks_left = (90 - user_age) * 52
month_left = (90 - user_age) * 12
day_left = (90 - user_age) * 365

print(f"You have {day_left} days, {weeks_left} weeks, {month_left} months left.")