import random

input = list(map(int, input().split(', ')))
arith = ['*','/','+','-']
answer = 0

while answer != input[-1]:
    random.shuffle(arith)
    answer = input[0]
    for i in range(len(arith)):
        if arith[i] == '*':
            answer *= input[i+1]
        elif arith[i] == '/':
            answer /= input[i+1]
        elif arith[i] == '+':
            answer += input[i+1]
        elif arith[i] == '-':
            answer -= input[i+1]

print(str(input[0]) + arith[0] + str(input[1]) + arith[1] + str(input[2]) + arith[2] + str(input[3]) + arith[3] + str(input[4]) + '=' + str(input[5]))