import sys

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

def f(pivot):
    cnt = 0
    for i in range(1, N+1):
        if pivot // i > N:
            cnt += N
        else:    
            cnt += pivot // i
        
    return cnt >= k
    # return ans <= pivot
    # B1<=B2<=...<=Bk <= pivot
    # pivot이하인 B의 원소가 k개 이상(Since B is sorted)
    # i * j <= pivot인 (i, j)의 개수 = cnt
    # cnt와 k를 비교

# parametric search to ans : 1~N^2
begin = 1
end = N * N
while begin < end:
    pivot = (begin + end) // 2
    if f(pivot) == True:
        end = pivot
    else:
        begin = pivot + 1

print(begin)

'''
답을 찾기는 어려움
하지만 답인지 아닌지 확인은 쉬움
-> binary search를 답에 쓴다.
-> 답이 될 수 있는 후보군이 1,2,3,....,N^2에 binary search.
-> 이를 parametric search라 한다.
'''