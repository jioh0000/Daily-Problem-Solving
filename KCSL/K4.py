row, column, distance = map(int, input().split(', '))
board = [[0]*5 for _ in range(5)]
column -= 1
row = 4 - (row-1)

for i in range(-distance, distance+1, 1):
    if row+i>=0 and row+i<=4:
        board[row+i][column] = 1
    if column+i>=0 and column+i<=4:
        board[row][column+i] = 1

for i in range(1,min(row, distance)+1):
    if column + i <= 4:
        board[row-i][column+i] = 1
    if column - i >= 0:
        board[row-i][column-i] = 1

for i in range(1,min(4-row, distance)+1):
    if column + i <= 4:
        board[row+i][column+i] = 1
    if column - i >= 0:
        board[row+i][column-i] = 1


count = 0
for i in board:
    for j in i:
        if j==0:
            count += 1

print(count) 