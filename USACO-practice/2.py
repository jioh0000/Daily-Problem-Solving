x, y = map(int, input().split())
amount = -0.5
moveCount = 0
prevPos = x
currentPos = x

while amount < abs(y-x):
    amount *= -2
    prevPos = currentPos
    currentPos = x + amount
    moveCount += abs(currentPos - prevPos)

print(int(moveCount - abs(currentPos - y)))