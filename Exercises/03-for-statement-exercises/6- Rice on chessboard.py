# Rice on chessboard
squares = 64
total = 0
grains = 1
for i in range(squares):
    total += grains
    grains *= 2
print(f"{total} number of grains.")