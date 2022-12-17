input = list(map(int, input().split(" ")))
ans = []
remainX = 0
remainY = 0
# input[0] = row, input[1] = column, input[2] = start, input[3] = # of blocks, 나머지 = positions of blocks

arr = [0] * (input[0] * input[1])
for i in range(input[3]):
    arr[input[4+i] - 1] = 2

currPos = input[2] - 1
while True:
    remainX = input[1] - 1 - (currPos%input[1])
    remainY = input[0] - 1 - (currPos//input[1])
    if remainX == 0: break
    try:
        if arr[currPos] + arr[currPos + 1] + arr[currPos + 2] == 0 and remainX >= 3:
            currPos += 2
            ans.append('A')
    except IndexError:
        pass

    remainX = input[1] - 1 - (currPos%input[1])
    remainY = input[0] - 1 - (currPos//input[1])
    if remainX == 0: break
    try:
        if arr[currPos + 1 + input[1]] + arr[currPos + 2 + input[1]] + arr[currPos + 1] == 0 and remainY >= 1:
            currPos += (input[1] + 2)
            ans.append('B')
    except IndexError:
        pass
   
    remainX = input[1] - 1 - (currPos%input[1])
    remainY = input[0] - 1 - (currPos//input[1])
    if remainX == 0: break
    try:
        if arr[currPos + 1] + arr[currPos + 2] + arr[currPos + input[1] + 2] + arr[currPos + input[1]*2 + 2] == 0 and remainY >= 2:
            currPos += input[1]*2 + 2
            ans.append('C')
    except IndexError:
        pass
    print(ans, remainX, remainY, currPos)

print(ans)
