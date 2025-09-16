# Chessboard
letters = "ABCDEFGH"

first_row = [letter+"1" for letter in letters]
print(f"{first_row}\n")

chessboard = []
print("Chessboard:")
for i in range(1, 9):               # Could have used list comprehension but im still not good at it
    row = []
    for letter in letters:
        row.append(f"{letter}{i}")
    chessboard.append(row)

for row in chessboard:
    print(row)