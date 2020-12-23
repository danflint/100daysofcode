"""
The program shows the highest score into list typed by user.
"""

scores = input("Input a list of students score,for example 22 55 44\n").split()
#convert string to integer list
scores = [int(score) for score in scores]

heighest_score = 0
for score in scores:
    if heighest_score < score: heighest_score = score

print(f"The highest score is equal to {heighest_score}.")