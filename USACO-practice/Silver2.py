t = input()
substring = []
a = ['b','e','s','s','i','e']

i = 0
ans = 0
while i < len(t):
    start = -1; end = -1
    if t[i] == 'b':
        start = i
        end = i
        j = 0
        while end < len(t):
            if a[j] == t[end]:
                j += 1
            if j == 6:
                break
            end += 1
        if j == 6:
            start = end
            j = 5
            while True:
                if t[start] == a[j]:
                    j -= 1
                if j < 0:
                    break
                start -= 1

            ans += (start + 1) * (len(t) - end)

            i = end
        
    i += 1
print(ans)
        
    
    