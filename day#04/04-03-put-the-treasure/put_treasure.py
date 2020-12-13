"""
    Put the trasure on matrix 3x3
"""
row1 = ["_", "_", "_"]
row2 = ["_", "_", "_"]
row3 = ["_", "_", "_"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")


#row/column
print("Hide your trasure. Choose the place where do you want to hide your treasure.")
tresure = input("row/column. example: 1,2\n")
treasure_position = tresure.split(",")
map[int(treasure_position[0])-1][int(treasure_position[1])-1] = "X"
print(f"{row1}\n{row2}\n{row3}\n")
