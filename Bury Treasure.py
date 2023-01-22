
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Example Column 1 Row 2 would be 12:  ")



C = int(position[0])-1
R = int(position[1])-1



map[R][C] = "X"


print(f"{row1}\n{row2}\n{row3}")

