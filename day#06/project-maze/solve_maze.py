"""
Solve the maze on the website https://reeborg.ca --> exc Maze
"""

def turn_right():
    for i in range(3):
        turn_left()

while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    elif not front_is_clear() and not wall_on_right():
        turn_right()
        move()
    elif not front_is_clear() and wall_on_right():
        turn_left()
    elif not wall_on_right():
        turn_right()
        move()
    elif front_is_clear():
        move()