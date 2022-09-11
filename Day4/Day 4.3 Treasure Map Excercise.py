row1 = ['🙂', '🙂', '🙂']
row2 = ['🙂', '🙂', '🙂']
row3 = ['🙂', '🙂', '🙂']
map = [row1, row2, row3]
print(f"{map[0]}\n{map[1]}\n{map[2]}\n")
position = int(input("Where do you want put the treasure?\n"))
col = position//10-1
row = position % 10-1
if col <= 2 and row <= 2:
    map[row][col] = '😵'
    print(f"{map[0]}\n{map[1]}\n{map[2]}\n")
else:
    print('Wrong position')