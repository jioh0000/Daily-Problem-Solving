A = input()
answer = 0
#ABCCABDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ

for i in range(0, len(A) - 1):
    if i == A.index(A[i]):
        storage = []
        index = i + 1
        while(A[index] != A[i]):
            storage.append(A[index])