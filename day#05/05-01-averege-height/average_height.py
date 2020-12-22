"""
The program counts average height you typed.
"""

students_heights = input("Input a height of studetns separate by space\n").split()
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])

#average height
average_height = 0
for student_height in students_heights:
    average_height += student_height
average_height = average_height / len(students_heights)
print(f"Average heights of studens is equal to: {average_height}cm.")