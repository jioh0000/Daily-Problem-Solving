N, K = map(str, input().split(', '))

if N == 'DIVIDE':
    print(K[0:4]*2 + " and " + K[4:8]*2)
elif N[0:-1] == 'ADD':
    i = int(N[-1])
    print(K[0:i] + K[0:-i])
elif N[0:-1] == 'SUBTRACT':
    i = int(N[-1])
    print(K[i:] + K[-3:])